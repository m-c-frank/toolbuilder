# ToolBuilder

ToolBuilder is a CLI tool written in Go. It parses a README.md file and creates files based on the specified paths and code blocks within the README.

## Installation

To compile ToolBuilder, you need to have Go installed. Save the Go code below to a file named `toolbuilder.go`.

## Usage

After compiling ToolBuilder, you can use it with the following command:

```sh
./toolbuilder -i README.md -o output_directory
```

Replace `README.md` with the path to your README and `output_directory` with the path where you want the files to be created.

## Compiling from Source

Run the following command in the directory with the `toolbuilder.go` source file:

```sh
go build -o toolbuilder toolbuilder.go
```

This will create a `toolbuilder` executable that you can run.

## Go Source Code for ToolBuilder

Save the following code to a file named `toolbuilder.go`.

## ./toolbuilder.go

```go
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
```

## License

ToolBuilder is released under the MIT License.
```

To use this README with `toolbuilder`, you would:

1. Compile `toolbuilder` from the provided Go source code.
2. Run `toolbuilder` with the README.md as input.
3. `toolbuilder` would then parse the README and create a `toolbuilder.go` file with the Go source code inside it.

Remember, this README is designed to be used with the `toolbuilder` tool once it is compiled and ready to use. The Go code block is marked with `## ./toolbuilder.go`, which `toolbuilder` will recognize as a path and content to create a file from.
