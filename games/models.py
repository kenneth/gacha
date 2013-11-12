from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    server = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
