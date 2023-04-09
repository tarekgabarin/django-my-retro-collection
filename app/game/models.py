from django.db import models
from gameconsole.models import GameConsole
from publisher.models import Publisher
from django.conf import settings
from tag.models import Tag

class Game(models.Model):
    title = models.CharField(max_length=250)
    game_consoles_released_on = models.ManyToManyField(GameConsole, related_name="games_released_on_console")
    publisher_of_game = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="games_published", null=True, blank=True, default=None)
    release_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    players_that_own_game = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='games_owned_by_player')
    tags_for_game = models.ManyToManyField(Tag, related_name="games_with_tag")