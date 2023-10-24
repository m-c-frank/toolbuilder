import sys
import pytest
from toolbuilder.cli_tool import main

# Centralized function to set mock return values
def set_mocks(mocker, **kwargs):
    default_values = {
        "fetch_repository_content": "mock_content",
        "select_search_algorithm": "mock_algo",
        "craft_prompt": "mock_prompt",
        "iterative_solution": "mock_response",
        "get_analysis": "mock_analysis",
        "get_debugging_info": "mock_debug_info",
        "get_recommendations": "mock_recommendations"
    }
    
    for mock_name, default_value in default_values.items():
        mocker.patch(f"toolbuilder.cli_tool.{mock_name}", return_value=kwargs.get(mock_name, default_value))

@pytest.mark.parametrize("args, expected_output", [
    (["fetch", "tool1", "path/to/file"], "Content of path/to/file:\n mock_content"),
    (["select_algo", "context1"], "Recommended Algorithm: mock_algo"),
    (["craft", "context1", "query1", "algo1"], "Crafted Prompt: mock_prompt"),
    (["iterate", "context1", "query1"], "Response: mock_response"),
    (["-f", "path/to/file", "--analyze"], "Analysis:\n mock_analysis"),
    (["-f", "path/to/file", "--debug"], "Debugging Information:\n mock_debug_info"),
    (["-f", "path/to/file", "--recommend"], "Recommendations:\n mock_recommendations"),
    (["-f", "path/to/file"], "Content of path/to/file:\n mock_content"),
    (["-q", "query1", "-c", "context1"], "Response: mock_response")
])
def test_main_commands(mocker, capsys, args, expected_output):
    set_mocks(mocker)
    sys.argv = ["test_name"] + args
    main()
    captured = capsys.readouterr()
    assert expected_output in captured.out

def test_invalid_command(capsys):
    sys.argv = ["test_name"]
    main()
    captured = capsys.readouterr()
    assert "Please provide valid command or options!" in captured.out
