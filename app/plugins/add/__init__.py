import logging
from app.commands import Command
from app.plugins.history_manager import add_record  # Import the add_record function

class AddCommand(Command):
    def execute(self, *args):
        result = None  # Initialize result to ensure it's always defined
        if len(args) != 2:
            logging.error("Add command: Require exactly two arguments.")
            print("Error: Require exactly two arguments.")
            return result
        try:
            numbers = list(map(int, args))
            result = sum(numbers)
            logging.info(f"Add result: {result}")
            print(f"The result is: {result}")
            add_record(f"add {' '.join(args)}", result)
        except ValueError:
            logging.error("Add command: Invalid input, expected integers.")
            print("Error: Invalid input, expected integers.")
        return result
