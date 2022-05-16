from django.db import models
import json
# Create your models here.

class PollSets(models.Model):
    item_name = models.CharField(max_length=100)
    item_img = models.CharField(max_length=500)
    item_cat = models.CharField(max_length=100)
    votes = models.IntegerField(blank=True, default=0)

    def __str__(self):
      return self.item_name
    