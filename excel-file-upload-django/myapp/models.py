from django.db import models
from django.conf import settings

# Create your models here.
class Data(models.Model):
    application=models.CharField(max_length=80,blank=True,null=True)
    budget=models.IntegerField()
    valuation=models.IntegerField()

    def __str__(self):
        return self.application
