from rest_framework import serializers

from projects_api.models import Issue, Project, Contributor, choicesclass


class IssuesSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source="project", read_only=True)
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
        read_only_fields = ["author", "project_id", "created_time"]

    def create(self, validated_data):
        project_id = self.context["view"].kwargs["project_pk"]
        validated_data["project"] = Project.objects.get(id=project_id)
        validated_data["author"] = self.context["request"].user
        instance = super().create(validated_data)
        return instance

    def validate_assignee(self, value):
        """Check that assigned user is a project contributor."""
        queryset = Contributor.objects.filter(
            project__id=self.context["view"].kwargs["project_pk"],
            user__id=value.id,
            permission__gte=choicesclass.Permission.CONTRIBUTOR,
        )
        if queryset.exists():
            return value
        else:
            raise serializers.ValidationError(
                "Assigned user must be a contributor of this project."
            )
