# Local
import decimal

from utils import product_api
from utils.messages import Message


def validate_order(data, token):
    product_details = product_api.retrieve_product(data['product_id'])
    product_details_json = product_details.json()

    if product_details.status_code != 200:
        return product_details_json['errors'], 0, False

    if product_details_json['data']:
        if product_details_json['data']['stock'] < data['quantity']:
            return Message.ERR_ORDER_MORE_THAN_STOCK, 0, False

    product_api.reduce_product_stock(data['product_id'], data['quantity'],
                                     product_details_json['data']['stock'], token)

    return product_details_json['data'], decimal.Decimal(product_details_json['data']['price']) * data['quantity'], True
