"""Created by Vishal Dogra on 30-06-2020"""

from src import priceScrapingService, ALL_ENDPOINTS_MAP
from src.constants import BASE_URL
from prettytable import PrettyTable


print("\n[+] Welcome to the Myntra Product Price Scraper.")
while True:
    print("[+] Choose one of the following views to proceed with: ")
    empty_table = PrettyTable(['S.No.', 'Views'])
    for key, endpoint in ALL_ENDPOINTS_MAP.items():
        empty_table.add_row([key, endpoint.name])
    print(empty_table)
    print("Press C to exit....")
    user_input = input("\n[+] Enter your selection (S.No.): ")
    if user_input.upper() == "C":
        print("\n[+] Exiting....")
        break
    try:
        user_input = int(user_input)
    except ValueError:
        print('\n[-] Invalid input detected. Please retry.')
        continue
    if user_input not in ALL_ENDPOINTS_MAP.keys():
        print("\n[-] Error detected, no endpoint found with S.No.")
        continue
    priceScrapingService.fetch_products_and_details_from_url(
        base=BASE_URL,
        endpoints=ALL_ENDPOINTS_MAP.get(user_input).value
    )
