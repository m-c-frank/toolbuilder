# toolbuilder 🛠️

Empower your development process with `toolbuilder`, the avant-garde solution for tool creation and enhancement. Whether you're a developer seeking to design intricate software tools or a creative enthusiast with a penchant for innovation, `toolbuilder` is here to redefine your crafting journey.

---

## Dive into the world of toolbuilder

`toolbuilder` isn't just another Dockerized solution; it's a vision crafted for developers and creative minds. By harnessing the power of neural API and deploying a Docker-in-Docker approach, we've ensured a platform that supports iterative tool development and optimization. What does this mean for you? A seamless, efficient, and enriched user experience throughout your tool's lifecycle.

## Features 🌟

### 1. Iterative Tool Development 🔄

Benefit from a feedback-driven development process to continuously refine and upgrade your tool functionalities.

### 2. Neural API Integration 🧠

Tap into the advanced neural models for genuine, human-like interactions and guidance. Fetch content, understand contexts, and engage in organic conversations.

```python
# toolbuilder/api_interface.py

import os
import openai as neuralapi
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
    "analyze_content": "You are an expert in analyzing Python code. Examine the following content and provide insights.",
    "debug_content": "You are a debugging expert. Analyze the following Python code and provide debugging information.",
    "recommend_optimizations": "You are an optimization specialist. Review the following Python code and provide recommendations for optimization."
}


def get_analysis(content):
    return send_request(content, "analyze_content")

def get_debugging_info(content):
    return send_request(content, "debug_content")

def get_recommendations(content):
    return send_request(content, "recommend_optimizations")

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
    return response.choices[0].message["content"]

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
```

### Example Output

when running this file with the directory structure of this readme and the file path set to api_interface.py
this is the resulting output:

```python
# toolbuilder/api_interface.py

import os
import openai as neuralapi
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
    "analyze_content": "You are an expert in analyzing Python code. Examine the following content and provide insights.",
    "debug_content": "You are a debugging expert. Analyze the following Python code and provide debugging information.",
    "recommend_optimizations": "You are an optimization specialist. Review the following Python code and provide recommendations for optimization."
}


def get_analysis(content):
    return send_request(content, "analyze_content")

def get_debugging_info(content):
    return send_request(content, "debug_content")

def get_recommendations(content):
    return send_request(content, "recommend_optimizations")

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
    return response.choices[0].message["content"]

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
```

### 3. Enhanced CLI 🖥️

Interact via an intuitive command-line interface, perfect for tool creation, tweaks, and user queries.

### 4. Safety Through Containers 🛡️

Experience the Docker-in-Docker setup, ensuring both consistency in tool behavior and robust security.

### 5. Iterative Response Refinement 📝

Work hand-in-hand with the AI. Every response from the neural API can be opened in an editor, like `vim`, for on-the-spot modifications. Once you're satisfied with the edits, simply exit the editor to let the program seamlessly continue its operations. Experience the luxury of real-time adjustments and tailor the AI outputs precisely to your needs.

---

## Getting Started

**Peek Inside - Directory Structure**:

```bash
.
├── LICENSE.md
├── README.md
├── toolbuilder
│   ├── templates
│   │   ├── file_retrieval.ppt
│   ├── __main__.py
│   ├── api_interface.py
│   ├── cli_tool.py
│   ├── docker_config.py
│   ├── feedback_optimizer.py
├── requirements.txt
├── Dockerfile
├── DinD.Dockerfile
└── tests
    ├── __init__.py
    ├── test_api_interface.py
    ├── test_cli_tool.py
    └── test_feedback_optimizer.py
```

## Installation & Usage 🛠️

1. **Clone** and access:

   ```bash
   git clone https://github.com/m-c-frank/toolbuilder.git
   cd toolbuilder
   ```

2. **Docker Build**:

   ```bash
   docker build -t toolbuilder -f Dockerfile .
   ```

   For Docker-in-Docker:

   ```bash
   docker build -t toolbuilder-dind -f DinD.Dockerfile .
   ```

3. **Kickstart** the Docker container:

   ```bash
   docker run -it --privileged --env NEURAL_API_KEY=your_api_key toolbuilder-dind
   ```

4. **Engage** with `toolbuilder`:

   ```bash
   toolbuilder-cli "Enter your command or inquiry"
   ```

## Companion Tools 🚀

Delve deeper into our ecosystem:

- **[dirbuilder](https://github.com/m-c-frank/dirbuilder)**
- **[workflowlibrary](https://github.com/m-c-frank/workflowlibrary)**
- **[noteutilsyncer](https://github.com/m-c-frank/noteutilsyncer)**
- **[conceptsplitter](https://github.com/m-c-frank/conceptsplitter)**
- **[textdownloader](https://github.com/m-c-frank/textdownloader)**
- **[contenttree](https://github.com/m-c-frank/contenttree)**

---

## Join the Evolution! 🌱

Contribute to `toolbuilder` and be a part of its evolution. Open issues, recommend enhancements, or submit a pull request. We appreciate your collaboration!

---

### Credits & Acknowledgements 🙏

Brought to life by [Martin Christoph Frank](https://github.com/m-c-frank). For assistance or queries: 💌 [martin7.frank7@gmail.com](martin7.frank7@gmail.com)

---

🔓 **License**: Explore our [GOS License](https://github.com/m-c-frank/toolbuilder/blob/main/LICENCE.md) to understand how `toolbuilder` thrives in the open-source community.
