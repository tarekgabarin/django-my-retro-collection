from django.urls import path
from publisher.views import UpdateRetrieveDeletePublisher, CreateTagOrGetListOfPublishers

urlpatterns = [
    path('', CreateTagOrGetListOfPublishers.as_view(), name="create_get_list_publisher"),
    path('<int:pk>/', UpdateRetrieveDeletePublisher.as_view(), name="get_update_delete_publisher")
]