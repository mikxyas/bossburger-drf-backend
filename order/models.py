from django.db import models
from location.models import Location
from accounts.models import User
from menu.models import MenuItem

class Order(models.Model):
    order = models.ManyToManyField(MenuItem)
    time_of_order = models.DateTimeField(auto_now_add=True)
    time_of_delivery = models.TimeField(null=True)
    Food_price = models.IntegerField(default=0)
    delivery_price = models.IntegerField(default=0)
    delivered = models.BooleanField(default=False)
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE, null=True)
    customer_location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE, null=True)
    PICKUP = 'PCK'
    DELIVERY = 'DVY'
    order_type_choices = [
        (PICKUP, 'Pickup'),
        (DELIVERY, 'Delivery'),
    ] 
    order_type = models.CharField(
        max_length=3, choices=order_type_choices, default=DELIVERY
    )
    quantities = models.JSONField()
    customer_phone = models.CharField(max_length=15, default='+251')
    def __str__(self):
        return str(self.customer)
        