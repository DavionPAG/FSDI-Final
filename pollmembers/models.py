
from django.db import models

# Create your models here.

class Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    age = models.IntegerField(null=True, blank=True)
    profile_picture = models.TextField()
    active = models.BooleanField(default=True)
    cohort = models.ForeignKey("Cohort", on_delete=models.SET_NULL, null=True)

class Cohort(models.Model):
    name = models.CharField(max_length=50)
