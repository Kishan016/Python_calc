import logging
from app.commands import Command
from app.plugins.history_manager import add_record

class SubCommand(Command):
    def execute(self, *args):
        try:
            numbers = list(map(int, args))
            result = numbers[0] - sum(numbers[1:])
            logging.info(f"Sub result: {result}")
            print(f"The result is: {result}")
            add_record(f"sub {' '.join(args)}", result)
        except ValueError:
            logging.error("Sub command: Invalid input, expected integers.")
            print("Error: Invalid input, expected integers.")
        return result
