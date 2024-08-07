"""
Order APIs
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

import traceback

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

# Local
from orders.models import Order
from utils.response import get_response
from log.defines import save_log
from utils.messages import Message
from utils import product_api
from orders.serializers import OrderSerializer
from orders.validations import validate_order


class OrderRetrieveListCreateAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderSerializer
    api_name = 'OrderRetrieveListCreateAPI'

    def get(self, request, pk=None):
        try:
            if pk:
                try:
                    order = Order.objects.get(pk=pk)
                except Order.DoesNotExist:
                    return get_response(errors={'detail': Message.ERR_ORDER_NOT_FOUND})

                srz = self.serializer_class(order)

                return get_response(srz.data)

            orders = Order.objects.all()
            srz = self.serializer_class(orders, many=True)

            return get_response(srz.data)

        except Exception as e:
            save_log(request, 'ERR_GET', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})

    def post(self, request):
        try:
            data = request.data
            srz = self.serializer_class(data=data)

            if srz.is_valid():
                res, total_price, is_valid = validate_order(srz.validated_data, request.headers['Authorization'])

                if not is_valid:
                    return get_response(errors={'detail': res})

                srz.save(total_price=total_price)

                return get_response(srz.data)

            return get_response(errors=srz.errors)

        except Exception as e:
            save_log(request, 'ERR_POST', self.api_name, f'{e}\n{traceback.format_exc()}')
            return get_response(errors={'detail': Message.ERR_TRY})


