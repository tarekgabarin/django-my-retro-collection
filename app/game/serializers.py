from rest_framework import serializers
from gameconsole.serializers import GameConsoleSerializer
from publisher.serializers import PublisherSerializer
from tag.serializers import TagSerializer
from user.serializers import UserSerializer
from game.models import Game

class GameSerializer(serializers.ModelSerializer):
    game_consoles_released_on = GameConsoleSerializer(many=True)
    publisher_of_game = PublisherSerializer()
    players_that_own_game = UserSerializer(many=True)
    tags_for_game = TagSerializer(many=True)

    class Meta:
        model = Game
        fields = ['title', 'game_consoles_released_on', 'publisher_of_game', 'release_date', 'players_that_own_game', 'tags_for_game']