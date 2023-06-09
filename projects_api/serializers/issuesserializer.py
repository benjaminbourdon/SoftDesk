from rest_framework import serializers

from projects_api.models import Issue, Project


class IssuesSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(
        source="project", queryset=Project.objects
    )
    issue_id = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = Issue
        fields = [
            "issue_id",
            "title",
            "description",
            "project_id",
            "tag",
            "priority",
            "status",
            "assignee",
            "author",
            "created_time",
        ]
        read_only_fields = ["author"]
