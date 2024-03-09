import time as t
import json

import server.BankAPI.dns_bank_api as bank
import server.NetworkAPI.dns_network_api as net
import packet_parser as pp
import user_cache as uc

NET_ID = 100


def process_transaction():
    # Get the transaction from the network
    transaction = net.network_request(NET_ID)
    print(transaction)

    card_data, price, vendor_bank_id, time = pp.process_packet(transaction)
    print(card_data, price, vendor_bank_id, time)

    data = uc.retrieve_user_data(card_data)
    if data is not None:
        bank_id, bank_secure_code = json.loads(data)
        print(bank_id, bank_secure_code)

    else:
        print("Card not found")
        return

    # Update the bank with the transaction details
    bank.bank_transfer(bank_id, vendor_bank_id, bank_secure_code, price)


def main():
    print(bank.bank_status())
    while True:
        result = net.network_check(NET_ID)
        print(result)

        if int(result.split()[-1]) > 0:
            process_transaction()
        t.sleep(5)  # pause for 5 seconds


# Run the main function
if __name__ == "__main__":
    main()
