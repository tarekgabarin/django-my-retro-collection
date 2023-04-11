from rest_framework import serializers
from publisher.models import Publisher

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','name']
        model = Publisher