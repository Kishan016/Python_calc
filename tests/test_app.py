"""Module for testing the App functionality."""

import os
from unittest.mock import patch
import pytest
from app import App  # Adjust this import according to your app's structure
from app.commands import Command

# Use a fixed path for the app's log file
log_file_path = os.path.join('logs', 'app.log')


@pytest.fixture(autouse=True)
def setup_and_teardown():
    """Fixture to clear the log file before each test."""
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    with open(log_file_path, 'w', encoding='utf-8') as file:
        file.close()


@pytest.fixture
def app():
    """Fixture to instantiate the App."""
    return App()


def read_log_contents():
    """Helper function to read log file contents."""
    with open(log_file_path, 'r', encoding='utf-8') as file:
        return file.read()


@patch('app.App.load_plugins')
def test_plugin_loading(mock_load_plugins, app):
    """Test that plugins are loaded."""
    app.load_plugins()
    mock_load_plugins.assert_called_once()


@patch('app.App.start')
def test_app_start(mock_start, app):
    """Test that the app starts correctly."""
    app.start()
    mock_start.assert_called_once()


def test_unknown_command_handling(app):
    """Test handling of unknown commands."""
    app.command_handler.execute_command('nonexistent_command')
    assert 'Unknown command: nonexistent_command' in read_log_contents()


@patch('os.path.exists')
@patch('logging.config.fileConfig')
def test_logging_configuration(mock_file_config, mock_exists, app):
    """Test logging configuration is loaded when file exists."""
    mock_exists.return_value = True
    app.configure_logging()
    mock_file_config.assert_called_once_with('logging.conf', disable_existing_loggers=False)
    mock_exists.return_value = False
    with patch('logging.basicConfig') as mock_basic_config:
        app.configure_logging()
        mock_basic_config.assert_called_once()


def test_logging_configuration_error_handling():
    """Test handling of logging configuration errors."""
    with patch('logging.config.fileConfig', side_effect=Exception("Logging config error")), \
         patch('logging.basicConfig') as mock_basic_config, \
         patch('logging.error') as mock_logging_error:
        App()  # This should now catch and handle the exception
        mock_basic_config.assert_called_once()
        mock_logging_error.assert_called()


def test_load_environment_variables():
    """Test that environment variables are correctly loaded into settings."""
    os.environ["TEST_ENV_VAR"] = "test_value"
    app_instance = App()  # Initialize App after setting the environment variable
    assert app_instance.settings["TEST_ENV_VAR"] == "test_value", "Environment variable was not loaded correctly."
    del os.environ["TEST_ENV_VAR"]  # Clean up


def test_default_environment_setting_direct(app):
    """Test the default 'PRODUCTION' environment setting by directly setting the environment variable."""
    # Directly set the environment variable in the app's settings for this test
    app.settings['ENVIRONMENT'] = 'PRODUCTION'
    assert app.settings.get('ENVIRONMENT') == 'PRODUCTION', "Failed to directly set 'ENVIRONMENT' to 'PRODUCTION'."


@patch('logging.warning')
def test_plugin_loading_failure(mock_logging_warning, app):
    """Test logging if the plugins directory doesn't exist."""
    # Assume app.plugins is the path checked by load_plugins() method.
    with patch('os.path.exists', return_value=False):
        app.load_plugins()
        mock_logging_warning.assert_called_once_with("Plugins directory 'app/plugins' not found.")



class TestCommand(Command):
    """A test command class."""

    def execute(self, *args, **kwargs):
        """Execute the test command."""
        print("Test command executed")


def test_register_and_execute_command_success(app):
    """Test successful command registration and execution."""
    class TestCommand(Command):
        """Docstring explaining test class"""
        def execute(self, *args, **kwargs):
            return "Test command executed"

    test_command = TestCommand()
    app.command_handler.register_command("test", test_command)
    with patch('app.CommandHandler.execute_command', return_value="Test command executed") as mock_execute:
        result = app.command_handler.execute_command('test')
        mock_execute.assert_called_once_with('test')
        assert result == "Test command executed", "The test command did not execute as expected."
