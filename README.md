# toolbuilder

`toolbuilder` is an advanced Dockerized solution designed to assist developers in creating, improving, or deploying various tools. By integrating with the state-of-the-art neural API and leveraging a Docker-in-Docker approach, this container offers a platform for iterative tool development and enhancement, ensuring the most efficient user experience over time.

## Features

- **Iterative Tool Development**: Facilitates feedback-driven development to enhance tool functionalities.
- **Neural API Integration**: Seamless integration with advanced neural models for human-like interactions and assistance.
- **Enhanced CLI**: Provides an intuitive interface for user interactions, tool creation, and modifications.
- **Safety Through Containers**: Employs a Docker-in-Docker setup, guaranteeing consistency and security.
- **Interactive Shell**: Delivers an enriched experience for multi-command sessions and tool testing.

## Directory Structure

```bash
.
├── LICENSE.md
├── README.md
├── toolbuilder
│   ├── __init__.py
│   ├── __main__.py
│   ├── api_interface.py
│   ├── cli_tool.py
│   ├── command_parser.py
│   ├── docker_config.py
│   └── feedback_optimizer.py
├── requirements.txt
├── Dockerfile
├── DinD.Dockerfile
└── tests
    ├── __init__.py
    ├── test_api_interface.py
    ├── test_cli_tool.py
    └── test_feedback_optimizer.py
```

## Installation

Clone the repository and navigate to the project root:

```bash
git clone https://github.com/m-c-frank/toolbuilder.git
cd toolbuilder
```

Build the main Docker image:

```bash
docker build -t toolbuilder -f Dockerfile .
```

For Docker-in-Docker:

```bash
docker build -t toolbuilder-dind -f DinD.Dockerfile .
```

## Usage

1. Start the primary Docker container:

```bash
docker run -it --privileged --env NEURAL_API_KEY=your_api_key toolbuilder-dind
```

2. Within the container, utilize the CLI tool for neural model interactions and tool development:

```bash
toolbuilder-cli "Your command or inquiry here"
```

3. Provide feedback to improve tools:

```bash
toolbuilder-feedback "Your feedback regarding the last response or tool"
```

## Related Tools

<!--START_TOKEN-->
**Note Utilities Ecosystem**: A suite of tools designed to streamline and enhance note-taking and information processing workflows.

- **[dirbuilder](https://github.com/m-c-frank/dirbuilder)** - Builds a directory structure from `tree`
- **[workflowlibrary](https://github.com/m-c-frank/workflowlibrary)** - Centralizes and synchronizes tool listings across ecosystems.
- **[noteutilsyncer](https://github.com/m-c-frank/noteutilsyncer)** - Synchronizes the tool listings across READMEs.
- **[conceptsplitter](https://github.com/m-c-frank/conceptsplitter)** - Extract atomic concepts from text using the OpenAI API.
- **[textdownloader](https://github.com/m-c-frank/textdownloader)** - A browser extension for text dumps.
- **[contenttree](https://github.com/m-c-frank/contenttree)** - Prints a repository's tree structure and file content.
<!--END_TOKEN-->

## Contributing

If you're interested in contributing to `toolbuilder` or the larger Note Utilities ecosystem, we're eager to collaborate. Raise issues, suggest enhancements, or submit pull requests. Feel free to reach out directly with any inquiries!

## License

`toolbuilder` is open-source and licensed under the [GOS License](https://github.com/m-c-frank/toolbuilder/blob/main/LICENCE.md).

## Credits

Developed and maintained by [Martin Christoph Frank](https://github.com/m-c-frank). For questions or assistance, please email [martin7.frank7@gmail.com](martin7.frank7@gmail.com).
