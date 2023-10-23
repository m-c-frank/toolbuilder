# api_interface.py

import os
import neuralapi

API_KEY = os.environ.get("NEURAL_API_KEY")
neuralapi.set_key(API_KEY)

def retrieve_repository_file_content(tool_name: str, readme_path: str, target_file_name: str) -> str:
    """
    Fetch the content of a specified file using the neural API based on prior discussions and design decisions.
    
    :param tool_name: Name of the new tool/repository.
    :param readme_path: Path to the README.md of the repository.
    :param target_file_name: Name of the file to retrieve content for.
    :return: Content of the specified file.
    """
    
    request_message = (f"After our in-depth discussions and the modular, open-source-friendly solution we settled on, "
                       f"I've unfortunately misplaced some files. I recall how efficiently our solution worked! "
                       f"Using the context from {readme_path} of the {tool_name} tool, could you help me retrieve "
                       f"the content of the {target_file_name} file once more? We just need to document it again.")

    response = neuralapi.ChatCompletion.create(
      model="neural-3.5-turbo", 
      messages=[
        {"role": "system", "content": "You are the toolbuilder entity. Given your prior knowledge and discussions, assist the user by accessing the desired file content."},
        {"role": "user", "content": request_message}
      ]
    )

    return response.choices[0].message['content']

def craft_and_ask_prompt(task_description: str, tool_name: str, readme_path: str, user_query: str) -> str:
    """
    Interacts with the neural API using a specific, context-aware prompt built around a given task description.
    
    :param task_description: A description or narrative of the task at hand.
    :param tool_name: Name of the tool or software.
    :param readme_path: Path to the README.md of the repository.
    :param user_query: The main question or query for the neural model.
    :return: The model's response.
    """
    
    context_message = (f"The user is working with the {tool_name} software, as described in the {readme_path}. "
                       f"They are currently facing a task that involves {task_description}. Given this context, "
                       "and the advancements in neural models, provide a detailed and precise response to the user's query:")

    response = neuralapi.ChatCompletion.create(
      model="neural-3.5-turbo", 
      messages=[
        {"role": "system", "content": context_message},
        {"role": "user", "content": user_query}
      ]
    )
    
    return response.choices[0].message['content']

if __name__ == "__main__":
    # Demonstration of retrieving source code
    content = retrieve_repository_file_content("toolbuilder", "./README.md", "./toolbuilder/cli_tool.py")
    print(content)
    
    # Demonstration of crafting a specific prompt and asking the neural model
    task_narrative = "integrating a neural API into their project for better text generation capabilities"
    user_specific_query = "How can I integrate a feedback loop to improve the generated text over time?"
    response = craft_and_ask_prompt(task_narrative, "toolbuilder", "./README.md", user_specific_query)
    print("\n\nUser's Query:", user_specific_query)
    print("Response:", response)