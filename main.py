import requests
from getpass import getuser

def get_all_products(url):
    resp = requests.get(url)
    print(type(resp.json()))

    return resp.json() if resp.status_code == 200 else "An error as ocurred"


if __name__ == '__main__':
    print(f'Hello {getuser()}!')

    api_url = 'https://dummyjson.com/products'

    # TODO Consume a products API to get a json
    response = get_all_products(api_url)
