from rest_framework import serializers

from projects_api.models import Contributor, Project


class ContributorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user", "project", "permission", "role"]
        read_only_fields = ["project", "permission"]

    def create(self, validated_data):
        project_id = self.context["view"].kwargs["project_pk"]
        validated_data["project"] = Project.objects.get(id=project_id)
        instance = super().create(validated_data)
        return instance
