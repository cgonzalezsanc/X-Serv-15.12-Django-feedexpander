from django.db import models

# Create your models here.
    
class Tweet(models.Model):
    content = models.CharField(max_length=150)
    url = models.CharField(max_length=64)


