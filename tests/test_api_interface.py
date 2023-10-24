import pytest
from toolbuilder_cli import api_interface

# Sample response
sample_response = {
    "choices": [
        {
            "finish_reason": "stop",
            "index": 0,
            "message": {
                "content": "Sample Response, BFS",
                "role": "assistant"
            }
        }
    ]
}

def test_send_request_general(mocker):
    mocker.patch('openai.ChatCompletion.create', return_value=sample_response)
    result = api_interface.send_request("World Series 2020 location?", "general_request")
    assert result == "Sample Response, BFS"

def test_send_request_with_template(mocker):
    mocker.patch('openai.ChatCompletion.create', return_value=sample_response)
    mocker.patch('toolbuilder_cli.api_interface.load_prompt_template', return_value="<REPO_DIR_TREE> <REQUESTED_FILENAME>")
    
    result = api_interface.send_request("World Series 2020 location?", "fetch_repository_content", "mock_template")
    assert result == "Sample Response, BFS"

def test_fetch_repository_content(mocker):
    mocker.patch('openai.ChatCompletion.create', return_value=sample_response)
    mocker.patch('toolbuilder_cli.api_interface.load_prompt_template', return_value="<REPO_DIR_TREE> <REQUESTED_FILENAME>")
    
    content = api_interface.fetch_repository_content("toolbuilder", "mock_dir_tree", "mock_target_file_name")
    assert content == "Sample Response, BFS"

def test_select_search_algorithm(mocker):
    mocker.patch('openai.ChatCompletion.create', return_value=sample_response)
    
    algo = api_interface.select_search_algorithm("mock_context")
    assert algo in ["BFS", "DFS", "Best-First", "A*", "MCTS"]

def test_craft_prompt(mocker):
    mocker.patch('openai.ChatCompletion.create', return_value=sample_response)
    
    prompt = api_interface.craft_prompt("mock_context", "mock_query", "mock_algo")
    assert prompt == "Sample Response, BFS"

@pytest.mark.parametrize(
    "function_name,context,expected",
    [
        ("get_analysis", "Python code", "Sample Response, BFS"),
        ("get_debugging_info", "Python code with an error", "Sample Response, BFS"),
        ("get_recommendations", "Python code", "Sample Response, BFS"),
    ],
)
def test_specialized_functions(mocker, function_name, context, expected):
    mocker.patch('openai.ChatCompletion.create', return_value=sample_response)
    
    function = getattr(api_interface, function_name)
    result = function(context)
    assert result == expected
