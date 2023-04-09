from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.generic import ListView
from game.models import Game
from game.serializers import GameSerializer

#class GamesList(ListView):
#   permission_classes = [IsAuthenticated]
#    serializer_class = GameSerializer

 #   def get_queryset(self):
        
    
class GamesCollectionList(ListView):
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer

    def get_queryset(self):
        user = self.request.user
        games_collected_by_user_list = Game.objects.filter(players_that_own_game__in=[user]).order_by('title').distinct()
        return games_collected_by_user_list

#class GameDetail(generics.RetrieveA):

