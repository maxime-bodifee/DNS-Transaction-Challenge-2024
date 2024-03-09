import server.user_cache as uc
import json


def main():
    print("Time to sign up for a debit card!")
    name = input("What is your name? ")
    bank_id = input("What is your bank ID? ")
    bank_code = input("What is your bank security code? ")

    print("Your card is being processed...")
    uc.store_user_data(name, json.dumps({"bank_id": bank_id, "bank_code": bank_code}))


if __name__ == '__main__':
    main()
