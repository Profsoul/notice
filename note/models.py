from django.db import models

# Create your models here.
class Note(models.Model):
    Time = models.TimeField(auto_now_add=True)
    Date = models.DateField(auto_now_add=True)
    Source = models.CharField(max_length=60)
    Destination = models.CharField(max_length=60)
    Amount = models.IntegerField()
    Noon = models.CharField(max_length=5)
