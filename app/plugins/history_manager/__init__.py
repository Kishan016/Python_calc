import pandas as pd
import logging
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'
DATA_DIR.mkdir(exist_ok=True)
HISTORY_FILE = DATA_DIR / 'history.csv'

# Define the path for the history.csv file within the data directory
HISTORY_FILE = DATA_DIR / 'history.csv'

def check_or_create_history_file():
    if not HISTORY_FILE.exists():
        # If the file does not exist, create it with the appropriate columns
        pd.DataFrame(columns=['Operation', 'Result']).to_csv(HISTORY_FILE, index=False)
        logging.info('History file created.')

def load_history():
    check_or_create_history_file()
    return pd.read_csv(HISTORY_FILE)

def save_history(df):
    df.to_csv(HISTORY_FILE, index=False)
    logging.info('History saved.')

def add_record(operation, result):
    """Add a record of an operation and its result to the history."""
    df = load_history()
    new_row = pd.DataFrame([[operation, result]], columns=['Operation', 'Result'])
    updated_df = pd.concat([df, new_row], ignore_index=True)
    save_history(updated_df)
    logging.info(f'Record added: {operation} = {result}')

def clear_history():
    pd.DataFrame(columns=['Operation', 'Result']).to_csv(HISTORY_FILE, index=False)
    logging.info('History cleared.')

def delete_history():
    if HISTORY_FILE.exists():
        HISTORY_FILE.unlink()
        logging.info('History file deleted.')