from factory.django import DjangoModelFactory
from consolemaker.models import ConsoleMaker

class ConsoleMakerFactory(DjangoModelFactory):
    class Meta:
        model = ConsoleMaker
    
    name = "console_maker_name"