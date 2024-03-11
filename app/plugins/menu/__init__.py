from app.commands import Command
import logging

import logging

class MenuCommand(Command):
    def execute(self, *args):
        logging.info("Displaying menu of commands")
        commands = [
            {"command": "add", "description": "Add numbers"},
            {"command": "sub", "description": "Subtract numbers"},
            {"command": "multi", "description": "Multiply numbers"},
            {"command": "div", "description": "Divide numbers"},
            {"command": "exit", "description": "Exit the application"}
        ]
        for cmd in commands:
            print(f"{cmd['command']}: {cmd['description']}")


# class MenuCommand(Command):
#     def execute(self, *args):
#         logging.info("Menu command executed: Displaying available commands.")
#         commands = [
#             {"command": "add", "description": "Add numbers"},
#             {"command": "sub", "description": "Subtract numbers"},
#             {"command": "multi", "description": "Multiply numbers"},
#             {"command": "div", "description": "Divide numbers"},
#             {"command": "exit", "description": "Exit the application"}
#             # Add more commands as needed
#         ]
#         print("Available commands:")
#         for cmd in commands:
#             print(f"{cmd['command']}: {cmd['description']}")
