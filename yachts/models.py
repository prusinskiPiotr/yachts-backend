from django.db import models
from django.contrib.auth.models import User


class Yachts(models.Model):
    model_name = models.CharField(max_length=255)
    length = models.CharField(max_length=10)
    width = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    max_crew = models.IntegerField()
    berths = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Rentals(models.Model):
    from_date = models.DateField()
    to_date = models.DateField()
    insurance = models.BooleanField()
    yacht = models.ForeignKey(Yachts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
