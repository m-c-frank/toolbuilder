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

# This is a demonstration of how you can retrieve the source code of the api_interface.py file from its own repository.
if __name__ == "__main__":
    content = retrieve_repository_file_content("toolbuilder", "./README.md", "./toolbuilder/api_interface.py")
    print(content)
```

### Example Output

```python
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

# This is a demonstration of how you can retrieve the source code of the api_interface.py file from its own repository.
if __name__ == "__main__":
    content = retrieve_repository_file_content("toolbuilder", "./README.md", "./toolbuilder/api_interface.py")
    print(content)
```

### 3. Enhanced CLI 🖥️

Interact via an intuitive command-line interface, perfect for tool creation, tweaks, and user queries.

### 4. Safety Through Containers 🛡️

Experience the Docker-in-Docker setup, ensuring both consistency in tool behavior and robust security.

---

## Getting Started

**Peek Inside - Directory Structure**:

```bash
.
├── LICENSE.md
├── README.md
└── toolbuilder
    ├── __init__.py
    ├── __main__.py
    ├── api_interface.py
    ├── cli_tool.py
    ├── command_parser.py
    ├── docker_config.py
    └── feedback_optimizer.py
├── requirements.txt
├── Dockerfile
├── DinD.Dockerfile
└── tests
    ├── __init__.py
    ├── test_api_interface.py
    ├── test_cli_tool.py
    └── test_feedback_optimizer.py
```

### Installation & Usage 🛠️

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

---

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

Your ideas can shape the future of `toolbuilder`. If you have a feature in mind or spot something amiss, don't hesitate. Raise issues, recommend enhancements, or float a pull request. Our doors (and repositories) are always open!

---

### Credits & Acknowledgements 🙏

Brought to life by [Martin Christoph Frank](https://github.com/m-c-frank). Need assistance or have questions? 💌 [martin7.frank7@gmail.com](martin7.frank7@gmail.com)

---

🔓 **License**: Dive into our [GOS License](https://github.com/m-c-frank/toolbuilder/blob/main/LICENCE.md) to know more about how `toolbuilder` operates in the open-source realm.
