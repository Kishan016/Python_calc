"""This module contains test cases for the App class."""
from unittest.mock import patch
import pytest
from app import App

# Helper function to read log file content
def read_log_file():
    """Read the log file"""
    log_file_path = 'logs/app.log'
    with open(log_file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Helper function to clear the log file before each test
def clear_log_file():
    """"Clear Log File"""
    # pylint: disable=consider-using-with
    open('logs/app.log', 'w', encoding='utf-8').close()

@pytest.fixture(autouse=True)
def run_before_and_after_tests():
    """"Run befor and after test to clear log file"""
    # Setup: clear log file before each test
    clear_log_file()
    # This yields control back to the test function
    yield
    # Teardown: can add post-test cleanup steps here

def test_app_start_and_exit():
    """"Test app start and exit"""
    with pytest.raises(SystemExit) as exit_exception:
        with patch('builtins.input', side_effect=['exit']):
            app = App()
            app.start()
    log_contents = read_log_file()
    assert exit_exception.value.code == 0, "Application did not exit as expected."
    assert "Application started." in log_contents, "Expected 'Application started.' log message not found."
    assert "Application shutdown." in log_contents, "Expected 'Application shutdown.' log message not found."
