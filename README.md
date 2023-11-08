# toolbuilder

toolbuilder is a simple CLI tool that parses a README.md file and creates files based on the specified paths and code blocks within the README. It's designed to be a straightforward way to bootstrap configuration files and scripts from a single document.

## Installation

To install toolbuilder, run the following command in your terminal:

```bash
curl -s https://raw.githubusercontent.com/m-c-frank/toolbuilder/main/install.sh | bash
```

This command will download and execute the `toolbuilder.sh` script from the repository, which sets up the tool on your system.

## Usage

After installation, you can use toolbuilder by running the following command in a directory with a README.md file:

```bash
toolbuilder
```

This will parse the README.md in the current directory and create the files as described in the document.

## Example

The following is an example section that toolbuilder can parse and create a file from when executed.

## ./toolbuilder.sh

```bash
#!/bin/bash
# toolbuilder.sh
# This script parses a README.md file and creates files based on the code blocks.

parse_readme() {
    local readme_path="$1"
    local in_code_block=false
    local file_path=""
    local content=()

    while IFS= read -r line || [[ -n "$line" ]]; do
        if [[ "$line" =~ ^##\ .\/ ]]; then
            if [ "$in_code_block" = true ] && [ -n "$file_path" ]; then
                extract_and_write "$file_path" "${content[@]}"
                content=()
            fi
            file_path=$(echo "$line" | sed 's/^## \(.*\)/\1/')
            in_code_block=false
        elif [[ "$line" == '```'* ]]; then
            in_code_block=!$in_code_block
            if [ "$in_code_block" = false ] && [ -n "$file_path" ]; then
                extract_and_write "$file_path" "${content[@]}"
                file_path=""
                content=()
            fi
        elif [ "$in_code_block" = true ]; then
            content+=("$line")
        fi
    done < "$readme_path"
}

extract_and_write() {
    local path="$1"
    local content=("${@:2}")
    mkdir -p "$(dirname "$path")"
    printf "%s\n" "${content[@]}" > "$path"
}

# Main execution
if [ -f "README.md" ]; then
    parse_readme "README.md"
else
    echo "Error: README.md not found."
    exit 1
fi
```

To create the `toolbuilder.sh` script from this README, a user would run the installation one-liner provided at the top of the README.

## Note

- Ensure that the URL in the installation command points to the actual location of your `toolbuilder.sh` script in the repository.
- The `toolbuilder.sh` script assumes that the README.md file is well-formed and follows the structure specified in the example.
