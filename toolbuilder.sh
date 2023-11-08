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

