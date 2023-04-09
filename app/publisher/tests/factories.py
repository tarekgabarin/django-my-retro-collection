from factory.django import DjangoModelFactory
from publisher.models import Publisher

class PublisherFactory(DjangoModelFactory):
    class Meta:
        model = Publisher
    
    name = "publisher_name"