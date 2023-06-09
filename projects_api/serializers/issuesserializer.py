from rest_framework import serializers

from projects_api.models import Issue


class IssuesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "project",
            "status",
            "author",
            "assignee",
            "created_time",
            "comment_set",
        ]
