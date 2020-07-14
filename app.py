"""Created by Vishal Dogra on 30-06-2020"""

from src import priceScrapingService, ALL_ENDPOINTS_MAP
from src.constants import BASE_URL
from prettytable import PrettyTable


print("\n[+] Welcome to the Myntra Product Price Scraper.")
while True:
    try:
        print("\n[+] Choose one of the following views to proceed with: ")
        empty_table = PrettyTable(['S.No.', 'Options'])

        key_count = 0
        for key, endpoint in ALL_ENDPOINTS_MAP.items():
            entry = endpoint.name[0].upper() + endpoint.name[1:].lower()
            empty_table.add_row([key, entry])

        key_count = len(ALL_ENDPOINTS_MAP) + 1

        empty_table.add_row(["-------", "-------------------------"])
        empty_table.add_row([key_count, "Enter new endpoint"])

        print(empty_table)

        print("Press key 'E' or type 'Exit' to exit....")

        user_input = input("\n[+] Enter your selection (S.No.): ")

        if user_input.upper() == "E" or user_input.upper() == "EXIT":
            print("\n[+] Exiting....")
            break

        try:
            user_input = int(user_input)
        except ValueError:
            print('\n[-] Invalid input detected. Please retry.')
            continue

        if user_input != key_count and user_input not in ALL_ENDPOINTS_MAP.keys():
            print("\n[-] Error detected, no endpoint found. Please check your input")
            continue

        final_endpoint = ""
        if user_input == key_count:
            custom_endpoint = input("\n[*] Enter your custom endpoint:")
            custom_endpoint.replace("/", "") if "/" in custom_endpoint else None
            final_endpoint = custom_endpoint
        else:
            final_endpoint = ALL_ENDPOINTS_MAP.get(user_input).value

        priceScrapingService.fetch_products_and_details_from_url(
            base=BASE_URL,
            endpoints=final_endpoint
        )
    except Exception as e:
        print("\n[-] Invalid endpoint detected. Please try again with correct input.")
        print(e)
