import json
import shelve
import os

db_directory = os.path.join(os.path.dirname(__file__), '../../data')  # Append 'data' to root directory
db_path = os.path.join(db_directory, 'user_data.db')  # Construct the path to the database file

# Ensure the directory exists, create it if not
if not os.path.exists(db_directory):
    os.makedirs(db_directory)


def store_user_data(user_name, user_data):
    with shelve.open(db_path) as db:
        db[user_name] = user_data


def retrieve_user_data(user_name):
    with shelve.open(db_path) as db:
        if user_name in db:
            return db[user_name]
        else:
            return None


def add_user_transactions(user_id, transaction):
    with shelve.open(db_path) as db:
        if user_id in db:
            user_transactions = db[user_id]
            user_transactions.append(transaction)
            db[user_id] = user_transactions
        else:
            db[user_id] = [transaction]


def retrieve_user_transactions(user_id):
    with shelve.open(db_path) as db:
        if user_id in db:
            return db[user_id]
        else:
            return None


def add_user_points(user_name, points):
    with shelve.open(db_path) as db:
        if user_name in db:
            id, code, user_points = json.loads(db[user_name]).values()
            db[user_name] = json.dumps({"bank_id": id, "bank_code": code, "points": int(user_points) + points})
