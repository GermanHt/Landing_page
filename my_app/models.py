from django.db import models

# Register your models here.

class Car(models.Model):
    name = models.CharField(max_length=40)
    model = models.IntegerField()
