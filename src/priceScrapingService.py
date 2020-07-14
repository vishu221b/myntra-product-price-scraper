"""Created by Vishal Dogra on 30-06-2020"""

import requests
from .utils import construct_url
import re
import json
import math
from .constants import (
    SYSTEM_INFORMATION, USER_AGENT_CLIENT,
    USER_AGENT_CLIENT_VERSION, BASE_URL,
    DELIMITER)
from prettytable import PrettyTable


def get_url(kwargs):
    url = construct_url(kwargs)
    return url


def get_response_from_url(url):
    headers = {
        "User-Agent":
            "{}/{} ({}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36".format(
                USER_AGENT_CLIENT,
                USER_AGENT_CLIENT_VERSION,
                SYSTEM_INFORMATION
            ),
            "Referer": url
    }  # so that the target server thinks that the requests are being made using the browser
    response = requests.get(url, headers=headers, timeout=5)
    return response


def get_json_data(content):
    c = re.findall(r"<script>window.__myx = (.+?)</script>", content.text)
    return c


def get_page_limit_for_pagination(url):
    content = get_response_from_url(url)
    extracted_json = get_json_data(content)
    all_products_count = json.loads(
        extracted_json[0]).get(
        'searchData'
    ).get(
        'results'
    ).get(
        'totalCount'
    )
    total_pages_for_pagination = math.ceil(all_products_count / 50)  # since 50 products are displayed per page
    return total_pages_for_pagination


def fetch_products_and_details_from_url(**kwargs):
    complete_url = get_url(kwargs)
    page_limit_for_pagination = get_page_limit_for_pagination(complete_url)
    print("\n[+] Found {} pages with 50 products per page. What do you want to do?".format(
        page_limit_for_pagination))
    while True:
        print("\n[+]" + ("-" * 50) + "\n")
        print(
            "[+] 1.\t{}\n[+] 2.\t{}".format(
                "Parse products by page number",
                "Exit")
        )
        print("\n[+]" + ("-" * 50) + "\n")
        user_input = input("[+] Enter your selection(1/2): ")
        print("\n[+]" + ("-" * 50) + "\n")
        if user_input == '1':
            page_number = input("Enter the page number to list the products of (enter nothing for page 1): ")
            print("\n[+]" + ("-" * 50))
            try:
                if not page_number:
                    page_number = 1  # default set to the home page of the respective view
                if int(page_number) == 0 or int(page_number) > page_limit_for_pagination:
                    print("\n[-] Page number doesn't exist. Please check your input.")
                    continue
            except ValueError:
                print("\n[-] Invalid input detected, please enter a valid page number.")
                continue
            pr_table = PrettyTable(
                [
                    'Product Name',
                    'Product Category',
                    'Product Original Price (MRP)',
                    'Product\'s Discount Price',
                    'Product\'s Chargeable Price',
                    'Brand',
                    'Buy link',
                    'Rating'
                ]
            )
            print("\n[+] PAGE Number -> {}".format(page_number))
            content = get_response_from_url(complete_url + "?p={}".format(page_number))
            extracted_json = get_json_data(content)
            results = json.loads(
                extracted_json[0]).get(
                'searchData'
            ).get(
                'results'
            )
            all_products = results.get(
                'products'
            )
            for product in all_products:
                pr_table.add_row([
                    product.get('productName'),
                    product.get('category'),
                    product.get('mrp'),
                    product.get('discount'),
                    product.get('price'),
                    product.get('brand'),
                    BASE_URL + DELIMITER + product.get('landingPageUrl'),
                    round(product.get('rating'), 1)
                ]
                )
            print(pr_table, end="\n\n")

        elif user_input == '2':
            print("[+] Exiting...")
            break

        else:
            print("[-] Invalid Input detected, please enter a valid selection.")
