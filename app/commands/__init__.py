from abc import ABC, abstractmethod
import logging

class Command(ABC):
    """
    Base class for all commands.
    Each command should implement the execute method.
    """
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
        self.logger = logging.getLogger(__name__)  # Updated: Added self.logger initialization

    def register_command(self, command_name, command_object):
        if command_name in self.commands:
            self.logger.warning(f"Command '{command_name}' is already registered and will be overwritten.")  # Updated: Changed logging.warning to self.logger.warning
        self.commands[command_name] = command_object
        self.logger.info(f"Command '{command_name}' registered.")  # Updated: Changed logging.info to self.logger.info

    def find_command(self, command_name):
        return self.commands.get(command_name)

    def execute_command(self, cmd_input):
        parts = cmd_input.split()
        command_name = parts[0]
        args = parts[1:]  # Arguments for the command

        command = self.find_command(command_name)
        if command:
            try:
                command.execute(*args)
                self.logger.info(f"Executed command: {cmd_input}")  # Log command execution with full command input
            except Exception as e:
                self.logger.error(f"Error executing command '{command_name}': {e}")  # Updated: Changed logging.error to self.logger.error
        else:
            self.logger.error(f"Unknown command: {cmd_input}")  # Log unknown commands with full command input
