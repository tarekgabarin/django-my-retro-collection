from django.db import models

class ConsoleMaker(models.Model):
    name = models.CharField(max_length=250)
