"""
Order serializers
Mostafa Rasouli
mostafarasooli54@gmail.com
August 2024
"""

from rest_framework import serializers

# Local
from orders.models import Order
from utils.product_api import retrieve_product
from utils.messages import Message


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id', 'total_price')