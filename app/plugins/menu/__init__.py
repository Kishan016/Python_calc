from app.commands import Command
import logging

class MenuCommand(Command):
    def execute(self, *args):
        logging.info("Displaying menu of commands")
        commands = [
            {"command": "add", "description": "Add numbers"},
            {"command": "sub", "description": "Subtract numbers"},
            {"command": "multi", "description": "Multiply numbers"},
            {"command": "div", "description": "Divide numbers"},
            {"command": "history", "description": "View calculation history"},
            {"command": "clear_history", "description": "Clear calculation history"},
            {"command": "delete_history", "description": "Delete history file"},
            {"command": "exit", "description": "Exit the application"}
        ]
        for cmd in commands:
            print(f"{cmd['command']}: {cmd['description']}")
