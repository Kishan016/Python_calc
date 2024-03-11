import logging
from app.commands import Command

class MultiCommand(Command):
    def execute(self, *args):
        try:
            numbers = list(map(int, args))
            result = 1
            for num in numbers:
                result *= num
            logging.info(f"Multi result: {result}")
            print(f"The result is: {result}")
        except ValueError:
            logging.error("Multi command: Invalid input, expected integers.")
            print("Error: Invalid input, expected integers.")

# import logging
# from app.commands import Command

# class MultiCommand(Command):
#     def execute(self, *args):
#         if len(args) != 2:
#             logging.error("Multi command requires exactly two arguments")
#             return
#         try:
#             result = round(float(args[0]) * float(args[1]), 1)
#             logging.info(f"Multi result: {result}")
#         except ValueError:
#             logging.error("Error: All arguments must be numeric")
