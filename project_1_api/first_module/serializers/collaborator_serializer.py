from rest_framework import serializers
from first_module.models import Collaborator

class CollaboratorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Collaborator
        fields = ['id', 'name', 'email']