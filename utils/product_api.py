import requests


BASE_URL = 'http://127.0.0.1:8000'


def retrieve_product(pk):
    response = requests.get(f'{BASE_URL}/products/{pk}/')
    print(response.json())

    return response


def reduce_product_stock(pk, quantity, stock, token):
    data = {
        'stock': stock - quantity
    }
    headers = {
        'Authorization': token
    }

    response = requests.put(f'{BASE_URL}/products/{pk}/', headers=headers, json=data)

    return response
