import logging
import sys
from app.commands import Command

class ExitCommand(Command):
    def execute(self, *args):
        logging.info("Exit command: Application exit initiated.")
        print("Exiting application.")

# class ExitCommand(Command):
#     def execute(self, *args):
#         logging.info("Exiting...")
#         sys.exit(0)
