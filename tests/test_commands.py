"""Test-cases for testing commands."""

from unittest.mock import patch
from math import isclose
import pytest
import pandas as pd
from app.plugins.history_manager import (
    add_record,
    clear_history,
    load_history,
    save_history,
    delete_history,
)
from app.plugins.add import AddCommand
from app.plugins.sub import SubCommand
from app.plugins.multi import MultiCommand
from app.plugins.div import DivCommand
from app.plugins.exit import ExitCommand
from app.commands import Command, CommandHandler

# Test cases for the history manager functionalities
@patch('app.plugins.history_manager.pd.read_csv')
def test_load_history(mock_read_csv):
    """Test load_history function."""
    mock_read_csv.return_value = pd.DataFrame(columns=['Operation', 'Result'])
    load_history()
    mock_read_csv.assert_called_once()


@patch('app.plugins.history_manager.pd.DataFrame.to_csv')
def test_save_history(mock_to_csv):
    """Test save_history function."""
    df = pd.DataFrame(columns=['Operation', 'Result'])
    save_history(df)
    mock_to_csv.assert_called_once()


@patch('app.plugins.history_manager.load_history')
@patch('app.plugins.history_manager.save_history')
def test_add_record(mock_save_history, mock_load_history):
    """Test add_record function."""
    mock_load_history.return_value = pd.DataFrame(columns=['Operation', 'Result'])
    add_record('add 5 3', 8)
    mock_save_history.assert_called_once()


@patch('app.plugins.history_manager.pd.DataFrame.to_csv')
def test_clear_history(mock_to_csv):
    """Test clear_history function."""
    clear_history()
    mock_to_csv.assert_called_once()


@patch('pathlib.Path.exists', return_value=True)
@patch('pathlib.Path.unlink')
def test_delete_history_exists(mock_unlink, mock_exists):
    """Test delete_history function when file exists."""
    delete_history()
    mock_unlink.assert_called_once()


@patch('os.path.exists')
def test_delete_history_not_exists(mock_exists):
    """Test delete_history function when file does not exist."""
    mock_exists.return_value = False
    delete_history()  # os.remove should not be called, thus no need to mock it here


# Test cases for command functionalities
def test_add_command_success():
    """Test AddCommand class for successful addition."""
    command = AddCommand()
    assert command.execute("5", "3") == 8


@patch('builtins.print')
def test_add_command_error_handling(mock_print):
    """Test AddCommand with various error conditions."""
    command = AddCommand()
    command.execute("5")  # Too few args
    mock_print.assert_called_with("Error: Require exactly two arguments.")
    command.execute("5", "3", "2")  # Too many args
    command.execute("a", "b")  # Non-integer args
    mock_print.assert_any_call("Error: Invalid input, expected integers.")


def test_multi_command_success():
    """Test MultiCommand class for successful multiplication."""
    command = MultiCommand()
    assert command.execute("5", "3") == 15


@patch('builtins.print')
def test_multi_command_non_integer_args(mock_print):
    """Test MultiCommand with non-integer input."""
    command = MultiCommand()
    command.execute("a", "b")
    mock_print.assert_called_with("Error: Invalid input, expected integers.")


def test_sub_command_success():
    """Test SubCommand class for successful subtraction."""
    command = SubCommand()
    result = command.execute("5", "3")
    assert result == 2, "Expected subtraction result to be 2."


@patch('builtins.print')
def test_sub_command_error_handling(mock_print):
    """Test SubCommand with non-integer input."""
    command = SubCommand()
    command.execute("a", "b")
    mock_print.assert_called_with("Error: Invalid input, expected integers.")


def test_div_command_success():
    """Test DivCommand class for successful division."""
    command = DivCommand()
    assert command.execute("6", "3") == 2


def test_div_command_division_by_zero():
    """Test DivCommand class for division by zero."""
    command = DivCommand()
    with pytest.raises(ValueError):
        command.execute("5", "0")


def test_div_command_non_integer_args():
    """Test DivCommand class with non-integer input."""
    command = DivCommand()
    with pytest.raises(ValueError):
        command.execute("a", "b")


def test_div_command_with_floating_point():
    """Test DivCommand class with floating-point input."""
    command = DivCommand()
    assert command.execute("10.5", "2") == 5.25


@patch('sys.exit')
def test_exit_command(mock_exit):
    """Test ExitCommand class."""
    exit_command = ExitCommand()
    exit_command.execute()
    mock_exit.assert_called_once()


def test_div_command_recurring_decimal():
    """Test DivCommand class for division leading to a recurring decimal."""
    command = DivCommand()
    result = command.execute("10", "3")
    assert isclose(result, 3.3333, rel_tol=1e-4), "Result is not close to 3.3333"


@patch('logging.Logger.warning')
def test_register_duplicate_command(mock_warning):
    """Test registering a duplicate command."""
    handler = CommandHandler()
    command = AddCommand()
    handler.register_command('add', command)
    handler.register_command('add', command)  # Attempt to register again
    mock_warning.assert_called_once()


@patch('logging.Logger.error')
def test_execute_unknown_command(mock_error):
    """Test executing an unknown command."""
    handler = CommandHandler()
    handler.execute_command('unknown')
    mock_error.assert_called_once_with("Unknown command: unknown")


class FaultyCommand(Command):
    """A faulty command class for testing purposes."""

    def execute(self, *args): # pylint: disable=arguments-differ
        """Execute the faulty command."""
        raise ValueError("Faulty command executed.")


@patch('logging.Logger.error')
def test_faulty_command_execution(mock_error):
    """Test executing a faulty command."""
    handler = CommandHandler()
    faulty_command = FaultyCommand()
    handler.register_command('faulty', faulty_command)
    handler.execute_command('faulty')
    mock_error.assert_called_once()
