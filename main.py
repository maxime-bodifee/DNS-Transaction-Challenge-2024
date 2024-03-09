import BankAPI.dns_bank_api as bank
import NetworkAPI.dns_network_api as net
import asyncio

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
        await asyncio.sleep(5)  # pause for 5 seconds

# Run the main function
asyncio.run(main())
