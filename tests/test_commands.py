"""This is a docstring to test plugin commands"""
from unittest.mock import patch
import pytest
from app import App

# Helper function to read log file content
def read_log_file():
    """Function to read log file"""
    log_file_path = 'logs/app.log'
    with open(log_file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Helper function to clear the log file before each test
def clear_log_file():
    """Function to clear the log file"""
    # pylint: disable=consider-using-with
    open('logs/app.log', 'w', encoding='utf-8').close()

@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """Fixture to clear log file before each test"""
    clear_log_file()
    # This yields control back to the test function
    yield
    # Teardown: can add post-test cleanup steps here

def test_app_add_command():
    """Test case for the add command"""
    inputs = ['add 1 2', 'exit']
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit):
            app.start()
    log_contents = read_log_file()
    assert "Add result: 3" in log_contents, "Expected 'Add result: 3' log message not found."

def test_add_command_non_numeric_arguments():
    """Test case for the add command with non-numeric arguments"""
    inputs = ['add one two', 'exit']
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit):
            app.start()
    log_contents = read_log_file()
    assert "Add command: Invalid input, expected integers." in log_contents, "The add command should validate numeric arguments"

def test_app_subtract_command():
    """Test case for the subtract command"""
    inputs = ['sub 5 2', 'exit']
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit):
            app.start()
    log_contents = read_log_file()
    assert "Sub result: 3" in log_contents, "The subtract command did not produce the expected output"

def test_app_multiply_command():
    """Test case for the multiply command"""
    inputs = ['multi 3 4', 'exit']
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit):
            app.start()
    log_contents = read_log_file()
    assert "Multi result: 12" in log_contents, "The multiply command did not produce the expected output"

def test_app_divide_command():
    """Test case for the divide command"""
    inputs = ['div 8 2', 'exit']
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit):
            app.start()
    log_contents = read_log_file()
    assert "Div result: 4.0" in log_contents, "The divide command did not produce the expected output"

def test_divide_command_div_by_zero():
    """Test case for the divide command with division by zero"""
    inputs = ['div 20 0', 'exit']
    with patch('builtins.input', side_effect=inputs):
        app = App()
        with pytest.raises(SystemExit):
            app.start()
    log_contents = read_log_file()
    assert "Div command: Division by zero." in log_contents, "Divide by zero did not produce the expected output"
