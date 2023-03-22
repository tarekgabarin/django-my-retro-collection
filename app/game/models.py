from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=250)
    # game ownership is a many-to-many relations with user
    # the tag a game is in is one-to-many with game
    # the console the game is in is a one-to-many
    #  