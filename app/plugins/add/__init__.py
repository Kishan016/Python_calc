import logging
from app.commands import Command

class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            logging.error("Add command: Require exact two arguments.")
            print("Error: Require exact two arguments.")
            return
        try:
            numbers = list(map(int, args))
            result = sum(numbers)
            logging.info(f"Add result: {result}")
            print(f"The result is: {result}")
        except ValueError:
            logging.error("Add command: Invalid input, expected integers.")
            print("Error: Invalid input, expected integers.")
