import logging
from app.commands import Command
from app.plugins.history_manager import add_record  # Import the add_record function

class DivCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            logging.error("Div command: Require exact two arguments.")
            print("Error: Require exact two arguments.")
            raise ValueError("The div command requires exactly two arguments.") 

        try:
            numbers = list(map(float, args))
            if numbers[1] == 0:
                logging.error("Div command: Division by zero.")
                print("Error: Division by zero.")
                raise ValueError("Division by zero") 
            result = numbers[0] / numbers[1]
            logging.info(f"Div result: {result}")
            print(f"The result is: {result}")
            # Log the operation and its result
            add_record(f"div {' '.join(args)}", result)
        except ValueError:
            logging.error("Div command: Invalid input, expected numbers.")
            print("Error: Invalid input, expected numbers.")
            raise ValueError("Invalid Input")
        return result