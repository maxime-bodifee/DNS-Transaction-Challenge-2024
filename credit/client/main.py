import credit.server.api.user_cache as uc
import json


def main():
    print("Welcome to LVL 100 Mafia Credit Corporation")
    name = input("What is your username? ") + "@"
    bank_id = input("What is your bank ID? ")
    bank_code = input("What is your bank security code? ")

    print("Your card is being processed...")
    uc.store_user_data(name, json.dumps({"bank_id": bank_id, "bank_code": bank_code}))
    print(f"Account Made! Your username is: {name}")


if __name__ == '__main__':
    main()
