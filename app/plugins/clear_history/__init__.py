from app.commands import Command
import logging
# Adjust the import according to the new location of history_manager
from app.plugins.history_manager import clear_history

class ClearHistoryCommand(Command):
    def execute(self, *args):
        clear_history()
        print("History cleared.")
        logging.info("Cleared history")
