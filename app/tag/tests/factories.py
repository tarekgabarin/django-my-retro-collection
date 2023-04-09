from factory.django import DjangoModelFactory
from tag.models import Tag

class TagFactory(DjangoModelFactory):
    class Meta:
        model = Tag

    name = "tag_name"