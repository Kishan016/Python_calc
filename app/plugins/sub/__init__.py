import logging
from app.commands import Command

class SubCommand(Command):
    def execute(self, *args):
        try:
            numbers = list(map(int, args))
            result = numbers[0] - sum(numbers[1:])
            logging.info(f"Sub result: {result}")
            print(f"The result is: {result}")
        except ValueError:
            logging.error("Sub command: Invalid input, expected integers.")
            print("Error: Invalid input, expected integers.")




# class SubCommand(Command):
#     def execute(self, *args):
#         if len(args) != 2:
#             logging.error("Sub command requires exactly two arguments")
#             return
#         try:
#             result = round(float(args[0]) - float(args[1]), 1)
#             logging.info(f"Sub result: {result}")
#         except ValueError:
#             logging.error("Error: All arguments must be numeric")
