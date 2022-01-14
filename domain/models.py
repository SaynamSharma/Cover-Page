from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    sugs = models.TextField()
    phone = models.CharField(max_length=100)
    date = models.DateField()