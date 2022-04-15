import requests


def get_req(url, params=None, headers=None):
    params = params or {}
    headers = headers or None
    response = requests.get(url=url, params=params, headers=headers)

    if response:
        return response.json()
    else:
        return response
