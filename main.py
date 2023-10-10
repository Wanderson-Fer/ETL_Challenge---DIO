import requests
import pandas as pd
from getpass import getuser

def get_all_products(url):
    resp = requests.get(url)
    # print(type(resp.json()))

    return resp.json(), resp.status_code


if __name__ == '__main__':
    print(f'Hello {getuser()}!')

    api_url = 'https://dummyjson.com/products'

    # Extration
    response, code = get_all_products(api_url)

    if code != 200:
        print(f'An error {code} as ocurred')

    df_product = pd.DataFrame(response['products'])

    # Transformation
    # Removing culumns
    df_product = df_product[[
        'title', 'description', 'price', 'discountPercentage',
        'rating', 'stock', 'brand', 'category'
    ]]

    agg_rule = {
        'price': 'mean',
        'discountPercentage': 'mean',
        'rating': 'mean',
        'stock': 'sum'
    }

    # Grouping by category
    df_product_by_category = df_product.groupby(
        ['category']
    ).agg(agg_rule).reset_index()

    # Grouping by brand
    df_product_by_brand = df_product.groupby(
        ['brand']
    ).agg(agg_rule).reset_index()

    # Loading (Data Mart)
    # TODO save the category and brand datas to excel

