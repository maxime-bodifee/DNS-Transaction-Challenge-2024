import shelve
import os

db_directory = os.path.join(os.path.dirname(__file__), 'data')  # Get the directory of main.py and append 'data'
db_path = os.path.join(db_directory, 'user_data.db')  # Construct the path to the database file

# Ensure the directory exists, create it if not
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

def store_user_data(user_id, user_code):
    with shelve.open(db_path) as db:
        db[user_id] = user_code

def retrieve_user_data(user_id):
    with shelve.open(db_path) as db:
        if user_id in db:
            return db[user_id]
        else:
            return None
