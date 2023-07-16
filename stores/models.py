from django.db import models

class Store(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
