import os
import openai as neuralapi
from tree_of_thoughts import OpenAILanguageModel, MonteCarloTreeofThoughts

# Constants for Configuration
API_KEY = os.environ.get("NEURAL_API_KEY")
API_MODEL = "gpt-3.5-turbo"
NUM_THOUGHTS = 1
MAX_STEPS = 3
MAX_STATES = 4
PRUNING_THRESHOLD = 0.5

FUNCTION_CONTEXTS = {
    "fetch_repository_content": "You are the toolbuilder entity. Given your prior knowledge and discussions, assist the user by accessing the desired file content.",
    "select_search_algorithm": "You are the algorithm strategist entity. Reflecting on our earlier interactions, deduce the best search algorithm suited for the presented context.",
    "craft_prompt": "You are the prompt artisan entity. Leveraging your understanding of the context and the chosen algorithm, design a compelling and effective prompt for the Tree of Thoughts algorithm.",
    "general_request": "You are a generalist AI, well-versed in multiple domains. Address the query with accurate and detailed information.",
}

def send_request(request_msg, function_name):
    context_msg = FUNCTION_CONTEXTS.get(
        function_name, FUNCTION_CONTEXTS["general_request"]
    )
    response = neuralapi.ChatCompletion.create(
        model=API_MODEL,
        messages=[
            {"role": "system", "content": context_msg},
            {"role": "user", "content": request_msg},
        ],
    )
    return response.choices[0].message["content"]

def fetch_repository_content(tool_name, readme_path, target_file_name):
    request_msg = (
        f"After our discussions and the modular solution we settled on, "
        f"Using context from {readme_path} of the {tool_name}, "
        f"write a new version of the {target_file_name} and give it to me in full"
    )
    return send_request(request_msg, "fetch_repository_content")

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
    content = fetch_repository_content(
        "toolbuilder", "./README.md", "./toolbuilder/cli_tool.py"
    )
    print("Fetched content:\n", content)

    context = input("Context: ")
    query = input("Query: ")
    response = iterative_solution(context, query)
    print("\nFinal Response:", response)
