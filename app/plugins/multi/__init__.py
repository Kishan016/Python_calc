import logging
from app.commands import Command
from app.plugins.history_manager import add_record

class MultiCommand(Command):
    def execute(self, *args):
        result = None  # Initialize result early
        try:
            numbers = list(map(int, args))
            result = 1
            for num in numbers:
                result *= num
            logging.info(f"Multi result: {result}")
            print(f"The result is: {result}")
            add_record(f"multi {' '.join(args)}", result)
        except ValueError:
            logging.error("Multi command: Invalid input, expected integers.")
            print("Error: Invalid input, expected integers.")
        return result
