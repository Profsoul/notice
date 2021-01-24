from django.db import models

# Create your models here.
class Note(models.Model):
    Time = models.TimeField(auto_now_add=True)
    Date = models.DateField(auto_now_add=True)
    Activity = models.CharField(max_length=60)
    Info = models.TextField(default=None)
    Status = models.CharField(max_length=30,default="Unfinished")
    Update = models.BooleanField(default=False)
