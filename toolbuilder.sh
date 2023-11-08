#!/bin/bash
# toolbuilder.sh
# This script parses a specified README.md file and creates files based on the code blocks.

show_help() {
    echo "Usage: toolbuilder [-h] [-i INPUT_PATH] [-o OUTPUT_PATH]"
    echo "  -h                Display this help message and exit."
    echo "  -i INPUT_PATH     Specify the path to the README.md file to parse."
    echo "  -o OUTPUT_PATH    Specify the root directory where files will be created."
}

parse_readme() {
    local readme_path="$1"
    local output_path="$2"
    local in_code_block=false
    local file_path=""
    local content=()

    while IFS= read -r line || [[ -n "$line" ]]; do
        if [[ "$line" =~ ^##\ .\/ ]]; then
            if [ "$in_code_block" = true ] && [ -n "$file_path" ]; then
                extract_and_write "$output_path/$file_path" "${content[@]}"
                content=()
            fi
            file_path=$(echo "$line" | sed 's/^## \(.*\)/\1/')
            in_code_block=false
        elif [[ "$line" == '```'* ]]; then
            in_code_block=!$in_code_block
            if [ "$in_code_block" = false ] && [ -n "$file_path" ]; then
                extract_and_write "$output_path/$file_path" "${content[@]}"
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

# Default paths
input_path="README.md"
output_path="."

# Parse command line options
while getopts ":hi:o:" opt; do
    case ${opt} in
        h )
            show_help
            exit 0
            ;;
        i )
            input_path=$OPTARG
            ;;
        o )
            output_path=$OPTARG
            ;;
        \? )
            echo "Invalid Option: -$OPTARG" 1>&2
            show_help
            exit 1
            ;;
        : )
            echo "Invalid Option: -$OPTARG requires an argument" 1>&2
            exit 1
            ;;
        * )
            show_help
            exit 1
            ;;
    esac
done
shift $((OPTIND -1))

# Main execution
if [ ! -f "$input_path" ]; then
    echo "Error: README.md not found at path: $input_path"
    exit 1
fi

parse_readme "$input_path" "$output_path"

