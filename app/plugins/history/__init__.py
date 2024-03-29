from app.commands import Command
import logging
# Adjust the import according to the new location of history_manager
from app.plugins.history_manager import load_history

class HistoryCommand(Command):
    def execute(self, *args):
        df = load_history()
        if df.empty:
            print("No history available.")
        else:
            print(df.to_string(index=False))
        logging.info("Displayed history")
