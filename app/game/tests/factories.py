import factory
from game.models import Game
from publisher.tests.factories import PublisherFactory
import datetime

class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    title = "thats_the_name_of_game"

    @factory.post_generation
    def game_consoles_released_on(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for gameconsole in extracted:
                self.game_consoles_released_on.add(gameconsole)

    publisher_of_game = factory.SubFactory(PublisherFactory)
    release_date = datetime.date(1980, 1, 1)

    @factory.post_generation
    def players_that_own_game(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for player in extracted:
                self.players_that_own_game.add(player)

    @factory.post_generation
    def tags_for_game(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for tag in extracted:
                self.tags_for_game.add(tag)
