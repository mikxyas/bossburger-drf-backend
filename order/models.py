from django.db import models
from location.models import Location
from accounts.models import User
from menu.models import MenuItem

class Order(models.Model):
    order = models.ManyToManyField(MenuItem)
    time_of_order = models.DateTimeField(auto_now_add=True)
    time_of_delivery = models.TimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    customer = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE, null=True)
    customer_location = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return str(self.order)
        