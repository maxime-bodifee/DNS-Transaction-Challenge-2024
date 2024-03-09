import time
import json

import BankAPI.dns_bank_api as bank
import NetworkAPI.dns_network_api as net

NET_ID = 100

def update_bank(account_from, account_to, secure_code, amount):
    message = f"transfer\n{account_from}\n{secure_code}\n{amount}\n{account_to}"
    return bank.bank_custom(message)

def process_transactions():
    # Get the transaction from the network
    transaction = net.network_request(NET_ID)

    # Parse the transaction to get the necessary details
    transaction_details = json.loads(transaction)

    # Update the bank with the transaction details
    # This is a placeholder, replace it with actual update logic
    account_from = transaction_details["account_from"]
    account_to = transaction_details["account_to"]
    secure_code = transaction_details["secure_code"]
    amount = transaction_details["amount"]
    return update_bank(account_from, account_to, secure_code, amount)


def main():
    print(bank.bank_status())
    while True:
        result = net.network_check(NET_ID)
        print(result)
        time.sleep(5)  # pause for 5 seconds

# Run the main function
if __name__ == "__main__":
    main()
