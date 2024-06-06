from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=32)
    industry = models.CharField(max_length=40)

class Location(models.Model):
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)


