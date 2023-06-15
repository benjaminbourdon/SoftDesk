from rest_framework import serializers

from projects_api.models import Contributor

# Import direct, sans passer par serializer.__init__, afin d'éviter un import circulaire
from projects_api.serializers.permissionserializer import PermissionSerializer


class ContributorListSerializer(serializers.ModelSerializer):
    permission = PermissionSerializer()

    class Meta:
        model = Contributor
        fields = ["user", "permission", "role"]
