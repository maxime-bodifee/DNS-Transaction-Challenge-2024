import BankAPI.dns_bank_api as bank
import NetworkAPI.dns_network_api as net
import asyncio
import re

NET_ID = 100

# async def process_transactions():
#     # Get the transaction from the network
#     transaction = await net.network_request(NET_ID)
#
#     # Parse the transaction to get the necessary details
#     # This is a placeholder, replace it with actual parsing logic
#     transaction_details = transaction.split(',')


async def main():
    print(bank.bank_status())
    while True:
        print(await net.network_check(NET_ID))
        packet = await net.network_request()
        await asyncio.sleep(5)  # pause for 5 seconds

# Run the main function
asyncio.run(main())

def process_packet(packet):
    # Define regular expressions to match the desired patterns
    card_data_pattern = r"Card Data: {(.*?)}"
    price_pattern = r"Price: {(\d+)}"
    vendor_pattern = r"Vendor: {(.*?)}"
    time_pattern = r"Time: (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})"

    # Compile regular expressions
    card_data_regex = re.compile(card_data_pattern)
    price_regex = re.compile(price_pattern)
    vendor_regex = re.compile(vendor_pattern)
    time_regex = re.compile(time_pattern)
    
    # Find matches in the packet
    card_data_match = card_data_regex.search(packet)
    price_match = price_regex.search(packet)
    vendor_match = vendor_regex.search(packet)
    time_match = time_regex.search(packet)

    # Extract the matched data
    if card_data_match:
        card_data = card_data_match.group(1)
    if price_match:
        price = price_match.group(1)
    if vendor_match:
        vendor = vendor_match.group(1)
    if time_match:
        time = time_match.group(1)
    
    # Print the extracted data
    print("Card Data:", card_data)
    print("Price:", price)
    print("Vendor:", vendor)
    print("Time:", time)

    return card_data,price,vendor,time