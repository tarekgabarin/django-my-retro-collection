import django_filters
from game.models import Game

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = ['publisher_of_game', 'game_consoles_released_on', 'tags_for_game']