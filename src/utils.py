"""Created by Vishal Dogra on 30-06-2020"""


# receiving endpoints as list so that this function can be used ahead with multiple endpoints if needed
def construct_url(kwargs):
    base = kwargs.get('base')
    endpoint = kwargs.get('endpoints')
    url = base + endpoint[0]
    print("URL generated->", url)
    return url
