import logging
from app.commands import Command

class DivCommand(Command):
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            if numbers[1] == 0:
                logging.error("Div command: Division by zero.")
                print("Error: Division by zero.")
                return
            result = numbers[0] / numbers[1]
            logging.info(f"Div result: {result}")
            print(f"The result is: {result}")
        except ValueError:
            logging.error("Div command: Invalid input, expected numbers.")
            print("Error: Invalid input, expected numbers.")

# class DivCommand(Command):
#     def execute(self, *args):
#         if len(args) != 2:
#             logging.error("Div command requires exactly two arguments")
#             return
#         try:
#             if float(args[1]) == 0:
#                 logging.error("Can't division by zero")
#                 return
#             result = round(float(args[0]) / float(args[1]), 1)
#             logging.info(f"Div result: {result}")
#         except ValueError:
#             logging.error("Error: All arguments must be numeric")
