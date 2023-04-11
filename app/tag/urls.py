from django.urls import path
from tag.views import UpdateRetrieveDeleteTag, CreateTagOrGetListOfTag

urlpatterns = [
    path('', CreateTagOrGetListOfTag.as_view(), name="create_get_list_tag"),
    path('<int:pk>/', UpdateRetrieveDeleteTag.as_view(), name="get_update_delete_tag")
]