from rest_framework import serializers

from projects_api.models import Project


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
        ]
        read_only_fields = fields
