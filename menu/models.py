from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(default='Name',max_length=100)
    price = models.IntegerField(default=0)
    img = models.URLField(max_length=100, default='https://bit.ly/2G85fwJ')
    food_pic = models.ImageField(null=True, blank=True)
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

# class Open_Closed(models.Model):
#     open = models.BooleanField(default=True)
#     def save(self, *args, **kwargs):
#         state = Open_Closed.objects.all()
#         if not self.pk and Open_Closed.objects.exists():
#             raise ValidationError('There is can be only one JuicerBaseSettings instance')
#         return super(Open_Closed, self).save(*args, **kwargs)
