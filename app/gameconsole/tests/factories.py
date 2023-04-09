import factory
from gameconsole.models import GameConsole
from consolemaker.tests.factories import ConsoleMakerFactory

class GameConsoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GameConsole
    
    name = "console_name"
    maker_of_console = factory.SubFactory(ConsoleMakerFactory)
    name_code = "CODE"