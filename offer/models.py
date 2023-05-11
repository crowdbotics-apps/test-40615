from django.conf import settings
from django.db import models
class Offer(models.Model):
    'Generated Model'
    listing_id = models.ForeignKey("users.User",on_delete=models.CASCADE,related_name="offer_listing_id",)
    purchase_pruce = models.BigIntegerField()

# Create your models here.
