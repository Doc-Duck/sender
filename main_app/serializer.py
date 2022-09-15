from rest_framework.serializers import ModelSerializer
from .models import Clients


class ClientSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = ('number', 'code', 'tag')


class MessageListSerializer(ModelSerializer):
    class Meta:
        model = Clients
        fields = ('content', 'filters', 'end_time')