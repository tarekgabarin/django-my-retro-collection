from rest_framework import serializers
from gameconsole.models import GameConsole
from consolemaker.serializers import ConsoleMakerSerializer

class GameConsoleSerializer(serializers.ModelSerializer):
    maker_of_console = ConsoleMakerSerializer()

    class Meta:
        fields = ["id", "name", "maker_of_console", "name_code"]
        model = GameConsole
