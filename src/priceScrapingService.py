"""Created by Vishal Dogra on 30-06-2020"""

import requests
from .utils import construct_url
import re
import json
import math
from .constants import (
    SYSTEM_INFORMATION, USER_AGENT_CLIENT,
    USER_AGENT_CLIENT_VERSION, BASE_URL,
    DELIMITER )
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


def fetch_products_and_details_from_url(**kwargs):
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
    complete_url = get_url(kwargs)
    content = get_response_from_url(complete_url)
    extracted_json = get_json_data(content)
    print(len(extracted_json))
    results = json.loads(
        extracted_json[0]).get(
        'searchData'
    ).get(
        'results'
    )
    all_products = results.get(
        'products'
    )
    all_product_count = results.get(
        'totalCount'
    )
    total_pages_for_pagination = math.ceil(all_product_count/50)
    print(total_pages_for_pagination)
    for product in all_products:
        pr_table.add_row([
            product.get('productName'),
            product.get('category'),
            product.get('mrp'),
            product.get('discount'),
            product.get('price'),
            product.get('brand'),
            BASE_URL + DELIMITER + product.get('landingPageUrl'),
            product.get('rating')
        ]
        )
    print(pr_table)
