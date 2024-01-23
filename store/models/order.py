from django.db import models
from .user import User
from .product import Product
from .address import Address

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone_no = models.CharField(max_length=13)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    ordered_on = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def get_price(self):
        return (self.product.price * self.quantity)
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by("-ordered_on")