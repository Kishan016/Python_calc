"""This is a docstring to introduce Test-cases for testing commands"""
import unittest
from unittest.mock import patch
import pandas as pd
from app.plugins.history_manager import delete_history
from app.plugins.history_manager import (
    add_record,
    clear_history,
    load_history,
    save_history
)
from app.plugins.add import AddCommand
from app.plugins.sub import SubCommand
from app.plugins.multi import MultiCommand
from app.plugins.div import DivCommand
from app.plugins.exit import ExitCommand


class TestHistoryManager(unittest.TestCase):
    """
    Test class for history manager.
    """

    @patch('app.plugins.history_manager.pd.read_csv')
    def test_load_history(self, mock_read_csv):
        """
        Test load_history function.
        """
        # Setup the mock to return a specific DataFrame structure
        mock_read_csv.return_value = pd.DataFrame(columns=['Operation', 'Result'])
        load_history()
        mock_read_csv.assert_called_once()

    @patch('app.plugins.history_manager.pd.DataFrame.to_csv')
    def test_save_history(self, mock_to_csv):
        """
        Test save_history function.
        """
        df = pd.DataFrame(columns=['Operation', 'Result'])
        save_history(df)
        mock_to_csv.assert_called_once()

    @patch('app.plugins.history_manager.load_history')
    @patch('app.plugins.history_manager.save_history')
    def test_add_record(self, mock_save_history, mock_load_history):
        """
        Test add_record function.
        """
        mock_load_history.return_value = pd.DataFrame(columns=['Operation', 'Result'])
        add_record('add 5 3', 8)
        mock_save_history.assert_called_once()

    @patch('app.plugins.history_manager.pd.DataFrame.to_csv')
    def test_clear_history(self, mock_to_csv):
        """
        Test clear_history function.
        """
        clear_history()
        mock_to_csv.assert_called_once()

    @patch('os.path.exists')  # Patch os.path.exists
    @patch('os.remove')       # (Keep the patch for os.remove)
    def test_delete_history_exists(self, mock_remove, mock_exists):
        """
        Test delete_history function when file exists.
        """
        mock_exists.return_value = True
        delete_history()

    @patch('os.path.exists')
    def test_delete_history_not_exists(self, mock_exists):
        """
        Test delete_history function when file does not exist.
        """
        mock_exists.return_value = False
        delete_history()  # os.remove should not be called, thus no need to mock it here


class TestCommands(unittest.TestCase):
    """
    Test class for commands.
    """
    def test_add_command(self):
        """
        Test AddCommand class.
        """
        command = AddCommand()
        result = command.execute("5", "3")
        self.assertEqual(result, 8)

    def test_sub_command(self):
        """
        Test SubCommand class.
        """
        command = SubCommand()
        result = command.execute("5", "3")
        self.assertEqual(result, 2)

    def test_multi_command(self):
        """
        Test MultiCommand class.
        """
        command = MultiCommand()
        result = command.execute("5", "3")
        self.assertEqual(result, 15)

    def test_div_command(self):
        """
        Test DivCommand class for division and input validation.
        """
        command = DivCommand()

        # Test for successful division
        self.assertEqual(command.execute("6", "3"), 2)

        # Test for division by zero - expecting ValueError
        with self.assertRaises(ValueError):
            command.execute("5", "0")

        # Test for non-numeric input - expecting ValueError
        with self.assertRaises(ValueError):
            command.execute("a", "3")
        with self.assertRaises(ValueError):
            command.execute("5", "b")


    @patch('sys.exit')
    def test_exit_command(self, mock_exit):
        """
        Test ExitCommand class.
        """
        exit_command = ExitCommand()
        exit_command.execute()

        mock_exit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
