import requests
import pandas as pd
from getpass import getuser

def get_all_products(url):
    resp = requests.get(url)
    print(type(resp.json()))

    return resp.json(), resp.status_code


if __name__ == '__main__':
    print(f'Hello {getuser()}!')

    api_url = 'https://dummyjson.com/products'

    # TODO Consume a products API to get a json
    response, code = get_all_products(api_url)

    if code != 200:
        print(f'An error {code} as ocurred')

    df_product = pd.DataFrame(response['products'])
