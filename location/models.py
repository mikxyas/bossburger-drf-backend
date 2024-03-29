from django.db import models
from accounts.models import User

class Location(models.Model):
    neighborhood = models.CharField(max_length=50)
    latitude = models.CharField(max_length=100 )
    longitude = models.CharField(max_length=100 )
    locPrice = models.IntegerField(default=0)
    locDistance = models.IntegerField(default=0)
    locName = models.CharField(max_length=200)
    locDesc = models.CharField(max_length=355)
    locCreator = models.ForeignKey(User, related_name='locations',on_delete=models.CASCADE, null=True)
    def __str__(self):              
        return self.locName
    