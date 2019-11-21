"""Api models serializers."""
from api.models import Application
from rest_framework import serializers


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):
    """Application serializer."""

    class Meta:
        """Serializer options."""

        model = Application
        fields = ['id', 'name', 'key']
