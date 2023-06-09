from rest_framework import serializers

from projects_api.models import Comment, Issue


class CommentSerializer(serializers.ModelSerializer):
    author_user_id = serializers.PrimaryKeyRelatedField(source="author", read_only=True)
    issue_id = serializers.PrimaryKeyRelatedField(
        source="issue", queryset=Issue.objects
    )
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
