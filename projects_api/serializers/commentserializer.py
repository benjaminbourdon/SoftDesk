from rest_framework import serializers

from projects_api.models import Comment, Issue


class CommentSerializer(serializers.ModelSerializer):
    author_user_id = serializers.PrimaryKeyRelatedField(source="author", read_only=True)
    issue_id = serializers.PrimaryKeyRelatedField(source="issue", read_only=True)
    comment_id = serializers.IntegerField(source="id", read_only=True)

    class Meta:
        model = Comment
        fields = [
            "comment_id",
            "description",
            "issue_id",
            "author_user_id",
            "created_time",
        ]
        read_only_fiels = [
            "comment_id",
            "issue_id",
            "author_user_id",
            "created_time",
        ]

    def create(self, validated_data):
        issue_id = self.context["view"].kwargs["issue_pk"]
        validated_data["issue"] = Issue.objects.get(id=issue_id)
        validated_data["author"] = self.context["request"].user
        instance = super().create(validated_data)
        return instance
