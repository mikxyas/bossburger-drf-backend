from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    img = models.URLField()
    post_pic = models.ImageField(null=True, blank=True)
    desc = models.CharField(max_length=500)
    GIVEAWAY = 'GA'
    OFFER = 'OF'
    EVENT = 'EV'
    post_type_choices = [
        (GIVEAWAY, 'Giveaway'),
        (OFFER, 'Offer'),
        (EVENT, 'Event'),
    ]
    post_type = models.CharField(max_length=3, choices=post_type_choices, default=GIVEAWAY)
    content = models.CharField(max_length=1000, null=True)
