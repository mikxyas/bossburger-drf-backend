from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(default='Name',max_length=100)
    price = models.IntegerField(default=0)
    img = models.URLField(max_length=100, default='https://bit.ly/2G85fwJ')
    available = models.BooleanField(default=True)
    BURGER = 'BRG'
    FRIES = 'FRI'
    EXTRA = 'EXT'
    BEVERAGE = 'BVG'
    food_type_choices = [
        (BURGER, 'Burger'),
        (FRIES, 'Fires'),
        (EXTRA, 'Extra'),
        (BEVERAGE, 'Beverage')
    ] 
    food_type = models.CharField(
        max_length=3, choices=food_type_choices, default=BURGER
    )
    def __str__(self):
        return str(self.name)
        