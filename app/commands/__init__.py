from abc import ABC, abstractmethod
import logging

class Command:
    """
    Base class for all commands.
    Each command should implement the execute method.
    """
    def execute(self, *args, **kwargs):
        raise NotImplementedError("This method should be overridden by subclasses.")

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name, command_object):
        self.commands[command_name] = command_object

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
            except Exception as e:
                logging.error(f"Error executing command '{command_name}': {e}")
        else:
            logging.error(f"Unknown command: {command_name}")



# class Command(ABC):
#     @abstractmethod
#     def execute(self, *args):
#         """
#         Execute the command with the given arguments.

#         :param args: Arguments passed to the command
#         """
#         pass

# class CommandHandler:
#     def __init__(self):
#         self.commands = {}

#     def register_command(self, command_name: str, command: Command):
#         """
#         Register a command with the command handler.

#         :param command_name: The name of the command
#         :param command: The command instance
#         """
#         self.commands[command_name] = command
#         logging.info(f"Command '{command_name}' registered.")

#     def execute_command(self, command_name: str, *args):
#         """
#         Execute a command by name with the provided arguments.

#         :param command_name: The name of the command to execute
#         :param args: Arguments to pass to the command
#         """
#         try:
#             logging.info(f"Executing command '{command_name}' with arguments: {args}")
#             self.commands[command_name].execute(*args)
#         except KeyError:
#             logging.error(f"No such command: {command_name}")
#         except Exception as e:
#             logging.error(f"Error executing command '{command_name}': {e}")
