from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=20)
    niche=models.TextField(null=True)
    email=models.CharField(null=True,max_length=190)
    price=models.IntegerField(null=True)
    rate=models.FloatField(null=True)


    def __str__(self):
        return self.username


class Works(models.Model):
    username=models.CharField(max_length=122)
    works=models.CharField(max_length=1000)



# Create your models here.
