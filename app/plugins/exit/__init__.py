import logging
import sys
from app.commands import Command

class ExitCommand(Command):
    def __init__(self):
        self._should_exit = False

    def execute(self, *args, **kwargs):
        # Implementation logic for the command
        self._should_exit = True
        sys.exit(0)

    def should_exit(self):
        return self._should_exit
