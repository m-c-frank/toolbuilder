# toolbuilder/api_interface.py

import os
import neuralapi
from tree_of_thoughts import OpenAILanguageModel, MonteCarloTreeofThoughts

API_KEY = os.environ.get("NEURAL_API_KEY")
API_MODEL = "gpt-3.5-turbo"
NUM_THOUGHTS = 1
MAX_STEPS = 3
MAX_STATES = 4
PRUNING_THRESHOLD = 0.5
PROMPT_TEMPLATE_FILEPATH = "toolbuilder/templates/file_retrieval.ppt"

FUNCTION_CONTEXTS = {
    "fetch_repository_content": PROMPT_TEMPLATE_FILEPATH,
    "select_search_algorithm": "You are the algorithm strategist entity. Reflecting on our earlier interactions, deduce the best search algorithm suited for the presented context.",
    "craft_prompt": "You are the prompt artisan entity. Leveraging your understanding of the context and the chosen algorithm, design a compelling and effective prompt for the Tree of Thoughts algorithm.",
    "general_request": "You are a generalist AI, well-versed in multiple domains. Address the query with accurate and detailed information.",
    "get_analysis": "You are an expert in analyzing Python code. Examine the following content and provide insights.",
    "get_debugging_info": "You are a debugging expert. Analyze the following Python code and provide debugging information.",
    "get_recommendations": "You are an optimization specialist. Review the following Python code and provide recommendations for optimization."
}


def get_analysis(content):
    return send_request(content, "get_analysis")

def get_debugging_info(content):
    return send_request(content, "get_debugging_info")

def get_recommendations(content):
    return send_request(content, "get_recommendations")

def load_prompt_template(prompt_path):
    with open(prompt_path, 'r') as file:
        return file.read()

def process_template(template_content, dir_tree, requested_file_path):
    return template_content.replace('<REPO_DIR_TREE>', dir_tree).replace('<REQUESTED_FILENAME>', requested_file_path)

def send_request(request_msg, function_name, processed_template=None):
    context_source = FUNCTION_CONTEXTS.get(function_name, FUNCTION_CONTEXTS["general_request"])

    if function_name == "fetch_repository_content":
        context_msg = processed_template
    elif context_source.endswith('.ppt'):
        context_msg = load_prompt_template(context_source)
    else:
        context_msg = context_source

    response = neuralapi.ChatCompletion.create(
        model=API_MODEL,
        messages=[
            {"role": "system", "content": context_msg},
            {"role": "user", "content": request_msg},
        ],
    )
    
    # Check if the response is structured correctly
    if "choices" in response and isinstance(response["choices"], list) and response["choices"]:
        return response["choices"][0]["message"]["content"]
    else:
        # Handle the case where the response is not as expected
        raise Exception("Unexpected response format:", response)
        


def fetch_repository_content(tool_name, dir_tree, target_file_name):
    template_content = load_prompt_template(PROMPT_TEMPLATE_FILEPATH)
    processed_template = process_template(template_content, dir_tree, target_file_name)
    request_msg = f"{tool_name} | {target_file_name}"
    return send_request(request_msg, "fetch_repository_content", processed_template)

def select_search_algorithm(context):
    algorithms = ["BFS", "DFS", "Best-First", "A*", "MCTS"]
    request_msg = f"Considering our past engagements, which search algorithm from the list {algorithms} would best address the problem context: '{context}'?"
    response = send_request(request_msg, "select_search_algorithm")
    selected_algo = next((algo for algo in algorithms if algo in response), None)
    return selected_algo

def craft_prompt(context, query, algo):
    request_msg = (
        f"Drawing from our previous conversations and your understanding of {algo} within the Tree of Thoughts framework, "
        f"craft a prompt that would navigate the context: '{context}' to address the question: {query}"
    )
    return send_request(request_msg, "craft_prompt")

def iterative_solution(context, query):
    model = OpenAILanguageModel(api_key=API_KEY, api_model=API_MODEL)
    tree_of_thoughts = MonteCarloTreeofThoughts(model)

    algo = select_search_algorithm(context)
    prompt = craft_prompt(context, query, algo)
    solution = tree_of_thoughts.solve(
        initial_prompt=prompt,
        num_thoughts=NUM_THOUGHTS,
        max_steps=MAX_STEPS,
        max_states=MAX_STATES,
        pruning_threshold=PRUNING_THRESHOLD,
    )
    return solution

if __name__ == "__main__":
    dir_tree = input("Directory Structure: ")
    requested_file_path = input("File Path: ")

    content = fetch_repository_content(
        "toolbuilder", dir_tree, requested_file_path
    )
    print("Fetched file content:\n", content)

    context = input("Context: ")
    query = input("Query: ")
    response = iterative_solution(context, query)
    print("\nFinal Response:", response)

