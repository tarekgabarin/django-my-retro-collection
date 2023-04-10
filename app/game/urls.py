from django.urls import path
from game.views import GamesList, GamesCollectionList, RemoveFromCollection, AddToCollection

urlpatterns = [
    path('', GamesList.as_view(), name='get-games'),
    path('my_collection/', GamesCollectionList.as_view(), name='my-collection'),
    path('my_collection/add/', AddToCollection.as_view(), name='add-collection'),
    path('my_collection/remove/', RemoveFromCollection.as_view(), name='remove-collection')
]