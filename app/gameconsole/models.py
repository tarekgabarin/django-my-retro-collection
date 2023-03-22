from django.db import models

# Create your models here.
class GameConsole(models.Model):
    title = models.CharField(max_length=250)