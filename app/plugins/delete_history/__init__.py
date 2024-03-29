from app.commands import Command
import logging
# Adjust the import according to the new location of history_manager
from app.plugins.history_manager import delete_history

class DeleteHistoryCommand(Command):
    def execute(self, *args):
        delete_history()
        print("History file deleted.")
        logging.info("Deleted history file")
