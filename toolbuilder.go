package main

import (
	"bufio"
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"regexp"
	"strings"
)

func main() {
	var inputPath, outputPath string
	flag.StringVar(&inputPath, "i", "README.md", "Specify the path to the README.md file to parse.")
	flag.StringVar(&outputPath, "o", ".", "Specify the root directory where files will be created.")
	flag.Parse()

	if flag.NFlag() == 0 {
		fmt.Println("Usage: toolbuilder [-i INPUT_PATH] [-o OUTPUT_PATH]")
		flag.PrintDefaults()
		return
	}

	file, err := os.Open(inputPath)
	if err != nil {
		fmt.Printf("Error opening input file: %v\n", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	inCodeBlock := false
	var filePath string
	var content strings.Builder

	for scanner.Scan() {
		line := scanner.Text()

		if match, _ := regexp.MatchString(`^##\ .\/`, line); match {
			if inCodeBlock && filePath != "" {
				writeFile(outputPath, filePath, content.String())
				content.Reset()
			}
			filePath = strings.TrimSpace(strings.TrimPrefix(line, "## "))
			inCodeBlock = false
		} else if strings.Contains(line, "```") {
			inCodeBlock = !inCodeBlock
			if !inCodeBlock && filePath != "" {
				writeFile(outputPath, filePath, content.String())
				filePath = ""
				content.Reset()
			}
		} else if inCodeBlock {
			content.WriteString(line + "\n")
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Printf("Error reading input file: %v\n", err)
	}
}

func writeFile(root, path, content string) {
	fullPath := filepath.Join(root, path)
	os.MkdirAll(filepath.Dir(fullPath), os.ModePerm)
	err := os.WriteFile(fullPath, []byte(content), 0644)
	if err != nil {
		fmt.Printf("Error writing file %s: %v\n", fullPath, err)
	}
}

