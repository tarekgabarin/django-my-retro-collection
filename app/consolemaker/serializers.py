from rest_framework import serializers
from consolemaker.models import ConsoleMaker

class ConsoleMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsoleMaker
        fields = ['name']