from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from publisher.serializers import PublisherSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from publisher.models import Publisher
from rest_framework.mixins import CreateModelMixin, ListModelMixin


class UpdateRetrieveDeletePublisher(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == "PUT" or self.request.method == "DELETE":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()


class CreateTagOrGetListOfPublishers(GenericAPIView, ListModelMixin, CreateModelMixin):
    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = PublisherSerializer
    queryset = Publisher.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
