# toolbuilder/cli_tool.py

import argparse
from toolbuilder_cli.api_interface import (
    iterative_solution,
    fetch_repository_content,
    select_search_algorithm,
    craft_prompt,
    get_analysis,
    get_debugging_info,
    get_recommendations,
)


def main():
    parser = argparse.ArgumentParser(
        description="CLI tool for the Toolbuilder application."
    )
    subparsers = parser.add_subparsers(title="Commands", dest="command")

    # fetch command
    fetch_parser = subparsers.add_parser(
        "fetch", help="Fetch the content of a specific file from the repository."
    )
    fetch_parser.add_argument(
        "tool_name", type=str, help="Name of the tool in the repository."
    )
    fetch_parser.add_argument(
        "file_path", type=str, help="Path to the file within the repository."
    )

    # algo command
    algo_parser = subparsers.add_parser(
        "select_algo", help="Select the most appropriate algorithm based on context."
    )
    algo_parser.add_argument(
        "context",
        type=str,
        help="Context based on which algorithm needs to be selected.",
    )

    # craft command
    craft_parser = subparsers.add_parser(
        "craft", help="Craft a prompt based on context and algorithm."
    )
    craft_parser.add_argument(
        "context", type=str, help="Context for crafting the prompt."
    )
    craft_parser.add_argument(
        "query", type=str, help="Query for which the prompt is to be crafted."
    )
    craft_parser.add_argument(
        "algorithm",
        type=str,
        help="Algorithm based on which the prompt is to be crafted.",
    )

    # iterate command
    iterate_parser = subparsers.add_parser(
        "iterate", help="Run the iterative solution for a given context and query."
    )
    iterate_parser.add_argument(
        "context", type=str, help="Context for running the iterative solution."
    )
    iterate_parser.add_argument(
        "query", type=str, help="Query for which the iterative solution is to be run."
    )

    # Existing functionality preserved
    parser.add_argument("-q", "--query", type=str, help="Query for the neural model.")
    parser.add_argument(
        "-c", "--context", type=str, help="Context for the neural model."
    )
    parser.add_argument(
        "-f", "--file", type=str, help="Path of the file to retrieve content from."
    )
    parser.add_argument(
        "--analyze", action="store_true", help="Analyze the provided file's content."
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Get debugging information for the provided file's content.",
    )
    parser.add_argument(
        "--recommend",
        action="store_true",
        help="Get recommendations for the provided file's content.",
    )

    args = parser.parse_args()

    # Implement the new command functionality
    if args.command == "fetch":
        # Define the directory structure
        dir_tree = """
        ...
        """
        content = fetch_repository_content(args.tool_name, dir_tree, args.file_path)
        print(f"Content of {args.file_path}:\n", content)
    elif args.command == "select_algo":
        algo = select_search_algorithm(args.context)
        print(f"Recommended Algorithm: {algo}")
    elif args.command == "craft":
        prompt = craft_prompt(args.context, args.query, args.algorithm)
        print(f"Crafted Prompt: {prompt}")
    elif args.command == "iterate":
        response = iterative_solution(args.context, args.query)
        print(f"Response: {response}")

    # Retain existing functionality
    elif args.file:
        dir_tree = """
        ...
        """
        content = fetch_repository_content("toolbuilder", dir_tree, args.file)

        if args.analyze:
            print("Analysis:\n", get_analysis(content))
        elif args.debug:
            print("Debugging Information:\n", get_debugging_info(content))
        elif args.recommend:
            print("Recommendations:\n", get_recommendations(content))
        else:
            print(f"Content of {args.file}:\n", content)

    elif args.query and args.context:
        response = iterative_solution(args.context, args.query)
        print("Response:", response)
    else:
        print("Please provide valid command or options!")


if __name__ == "__main__":
    main()
