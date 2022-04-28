from django.db import models

# Create your models here.

class PollSets(models.Model):
    item_name = models.CharField(max_length=100)
    item_img = models.CharField(max_length=500)
    item_cat = models.CharField(max_length=100)
    votes = models.IntegerField(null=True)