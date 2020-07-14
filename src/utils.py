"""Created by Vishal Dogra on 30-06-2020"""

from src import constants


def construct_url(kwargs):
    base = kwargs.get('base')
    endpoint = kwargs.get('endpoints')
    url = base + constants.DELIMITER + endpoint
    print("URL generated->", url)
    return url
