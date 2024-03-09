import time as t
import json
import pandas as pd

import api.dns_bank_api as bank
import api.dns_network_api as net
import api.user_cache as uc
import util.packet_parser as pp

NET_ID = 100
CREDIT_ID = 4806489472053998958
CREDIT_CODE = 954998271


def print_user_transactions(user):
    uid, code, points = json.loads(uc.retrieve_user_data(user)).values()
    print(f"Transaction History for user {user}:")
    df = pd.DataFrame(columns=["Username", "Vendor", "Price", "Time"])
    for i, transaction in enumerate(uc.retrieve_user_transactions(uid)):
        username, vendor, price, time = json.loads(transaction).values()
        df.loc[i] = [username, vendor, float(price), time]
    print(df)
    print(f"Total Owed: {df['Price'].sum()}")
    print(f"Total Points: {points}")


def credit_transaction(user, price, vendor, time, user_bank_id, user_bank_code, vendor_bank_id, vendor_bank_code):
    bank.bank_transfer(CREDIT_ID, vendor_bank_id, CREDIT_CODE, float(price) * 0.1)
    print(f"Charged 90% fee, {vendor} received {float(price) * 0.1:.2f}")
    uc.add_user_transactions(user_bank_id, json.dumps({"user": user, "vendor": vendor, "price": price, "time": time}))
    uc.add_user_points(user, int(float(price) * 100))
    print_user_transactions(user)


def process_transaction():
    # Get the transaction from the network
    transaction = net.network_request(NET_ID)
    print(transaction)

    user, price, vendor, time = pp.process_packet(transaction)
    print(user, price, vendor, time)

    data = uc.retrieve_user_data(user)

    vendor_name = vendor[1:] if vendor.startswith("c") else vendor
    vendor_data = uc.retrieve_user_data(vendor_name)

    if data is None or vendor_data is None:
        return

    user_bank_id, user_bank_code, user_points = json.loads(data).values()
    print(user_bank_id, user_bank_code)

    vendor_bank_id, vendor_bank_code, vendor_points = json.loads(vendor_data).values()
    print(vendor_bank_id, vendor_bank_code)

    if vendor.startswith("c"):
        return credit_transaction(user, price, vendor_name, time, user_bank_id, user_bank_code, vendor_bank_id, vendor_bank_code)

    # Update the bank with the transaction details
    bank.bank_transfer(user_bank_id, vendor_bank_id, user_bank_code, price)


def main():
    print(bank.bank_status())
    while True:
        result = net.network_check(NET_ID)
        print("\n", result, "\n")

        if int(result.split()[-1]) > 0:
            process_transaction()
        t.sleep(5)  # pause for 5 seconds


# Run the main function
if __name__ == "__main__":
    main()
