import shelve
import os

db_directory = os.path.join(os.path.dirname(__file__), '../../data')  # Append 'data' to root directory
db_path = os.path.join(db_directory, 'user_data.db')  # Construct the path to the database file

# Ensure the directory exists, create it if not
if not os.path.exists(db_directory):
    os.makedirs(db_directory)

def store_user_data(user_name, user_code):
    with shelve.open(db_path) as db:
        db[user_name] = user_code

def retrieve_user_data(user_name):
    with shelve.open(db_path) as db:
        if user_name in db:
            return db[user_name]
        else:
            return None
