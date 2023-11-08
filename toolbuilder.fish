#!/usr/bin/env fish
# toolbuilder.fish
# This script parses a specified README.md file and creates files based on the code blocks.

function show_help
    echo "Usage: toolbuilder [-h] [-i INPUT_PATH] [-o OUTPUT_PATH]"
    echo "  -h                Display this help message and exit."
    echo "  -i INPUT_PATH     Specify the path to the README.md file to parse."
    echo "  -o OUTPUT_PATH    Specify the root directory where files will be created."
    echo "If no arguments are provided, this help message will be shown."
end

function parse_readme
    set readme_path $argv[1]
    set output_path $argv[2]
    set in_code_block false
    set file_path ""
    set content ""

    for line in (cat $readme_path)
        if string match -qr "^##\ ./" $line
            if test $in_code_block = "true" -a -n $file_path
                extract_and_write $output_path/$file_path $content
                set content ""
            end
            set file_path (string replace -r "^##\ (.*)" '$1' $line)
            set in_code_block false
        else if string match -q '```' $line
            set in_code_block (test $in_code_block = "false"; and echo "true"; or echo "false")
            if test $in_code_block = "false" -a -n $file_path
                extract_and_write $output_path/$file_path $content
                set file_path ""
                set content ""
            end
        else if test $in_code_block = "true"
            set content $content\n$line
        end
    end
end

function extract_and_write
    set path $argv[1]
    set content $argv[2..-1]
    command mkdir -p (dirname $path)
    echo -e $content > $path
end

# Check if no arguments were provided
if set -q argv[1]
    switch $argv[1]
        case '-h' '--help'
            show_help
            exit 0
        case '-i'
            set input_path $argv[2]
        case '-o'
            set output_path $argv[2]
        case '*'
            echo "Invalid Option: $argv[1]" >&2
            show_help
            exit 1
    end
else
    show_help
    exit 0
end

# Main execution
if not test -f $input_path
    echo "Error: README.md not found at path: $input_path"
    exit 1
end

parse_readme $input_path $output_path

