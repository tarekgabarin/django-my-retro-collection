from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from game.models import Game
from game.serializers import GameSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response


class GamesList(APIView):
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        query_parameters_of_call = request.query_params
        games_in_db = Game.objects.all()

        if "tags" in query_parameters_of_call:
            arr_of_tags_from_url = query_parameters_of_call["tags"].split(",")
            if len(arr_of_tags_from_url) == 1:
                games_in_db = games_in_db.filter(
                    tags_for_game__name__in=arr_of_tags_from_url
                )
            else:
                for tag in arr_of_tags_from_url:
                    games_in_db = games_in_db.filter(tags_for_game__name__in=[tag])

        if "consoles" in query_parameters_of_call:
            arr_of_consoles_from_url = query_parameters_of_call["consoles"].split(",")
            games_in_db = games_in_db.filter(
                game_consoles_released_on__name_code__in=arr_of_consoles_from_url
            )

        if "publisher" in query_parameters_of_call:
            games_in_db = games_in_db.filter(
                publisher_of_game__name=query_parameters_of_call["publisher"]
            )

        games_found = games_in_db.distinct()
        serializer = self.serializer_class(games_found, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCollection(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer
    http_method_names = ["put"]

    def put(self, request, *args, **kwargs):
        id_of_game_to_add = request.data["game_id"]
        added_game_obj = Game.objects.get(id=id_of_game_to_add)
        user = get_user_model().objects.get(id=request.user.id)
        user.games_owned_by_player.add(added_game_obj)
        user.save()
        titles_owned_by_player = user.games_owned_by_player.all()
        serializer = self.serializer_class(titles_owned_by_player, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RemoveFromCollection(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer
    http_method_names = ["put"]

    def put(self, request, *args, **kwargs):
        id_of_game_to_add = request.data["game_id"]
        added_game_obj = Game.objects.get(id=id_of_game_to_add)
        user = get_user_model().objects.get(id=request.user.id)
        user.games_owned_by_player.remove(added_game_obj)
        user.save()
        titles_owned_by_player = user.games_owned_by_player.all()
        serializer = self.serializer_class(titles_owned_by_player, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GamesCollectionList(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        games_collected_by_user_list = (
            Game.objects.filter(players_that_own_game__in=[user])
            .order_by("title")
            .distinct()
        )
        serializer = self.serializer_class(games_collected_by_user_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
