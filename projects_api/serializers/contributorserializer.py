from rest_framework import serializers

from projects_api.models import Contributor


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user"]

    def to_representation(self, instance):
        return {
            "id": instance.user.id,
            "username": instance.user.username,
        }
