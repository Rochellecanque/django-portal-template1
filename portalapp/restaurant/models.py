# restaurant/models.py

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
