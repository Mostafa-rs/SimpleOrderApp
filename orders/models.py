from django.db import models


class Order(models.Model):
    product_id = models.IntegerField()
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
