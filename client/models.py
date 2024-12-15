from django.db import models
class Profilecl(models.Model):
    username=models.CharField(max_length=122)
    password=models.CharField(max_length=20)
    niche=models.TextField()
    email=models.CharField(max_length=190)
   

    def __str__(self):
        return self.username
    
class Rating(models.Model):
    username=models.CharField(null=True,max_length=122)
    rate=models.IntegerField()

class Feedback(models.Model):
    username=models.CharField(null=True,max_length=122)
    feedback=models.TextField()

class Message(models.Model):
    user_sender=models.CharField(null=True,max_length=122)
    user_receiver=models.CharField(null=True,max_length=122)
    message=models.TextField()
    number=models.IntegerField(null=True)
    unread=models.BooleanField(null=True)



# Create your models here.
