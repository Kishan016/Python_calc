"""This module contains test cases for the App class."""
from unittest.mock import patch
import pytest
from app import App
import os

# Helper function to read log file content
def read_log_file():
    """Read the log file"""
    log_file_path = 'logs/app.log'
    with open(log_file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Helper function to clear the log file before each test
def clear_log_file():
    """Function to clear the log file."""
    log_directory = "logs"
    log_file_path = os.path.join(log_directory, "app.log")

    # Ensure the directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Ensure the file exists (create it if it doesn't) and then clear the file
    with open(log_file_path, 'a', encoding='utf-8') as f:
        pass  # Just to ensure the file is created

    with open(log_file_path, 'w', encoding='utf-8') as f:
        pass  # Clear the file

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
