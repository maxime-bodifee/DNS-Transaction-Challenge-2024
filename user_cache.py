import shelve

def store_user_data(user_id, user_code):
    with shelve.open('user_data.db') as db:
        db[user_id] = user_code

def retrieve_user_code(user_id):
    with shelve.open('user_data.db') as db:
        if user_id in db:
            return db[user_id]
        else:
            return None