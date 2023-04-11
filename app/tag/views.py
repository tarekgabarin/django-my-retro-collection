from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from tag.serializers import TagSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from tag.models import Tag
from rest_framework.mixins import CreateModelMixin, ListModelMixin

class UpdateRetrieveDeleteTag(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == "PUT" or self.request.method == "DELETE":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class CreateTagOrGetListOfTag(GenericAPIView, ListModelMixin, CreateModelMixin):
    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = TagSerializer
    queryset = Tag.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
