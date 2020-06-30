"""Created by Vishal Dogra on 30-06-2020"""


def construct_url(kwargs):
    base = kwargs.get('base')
    endpoint = kwargs.get('endpoints')
    url = base + endpoint
    print("URL generated->", url)
    return url
