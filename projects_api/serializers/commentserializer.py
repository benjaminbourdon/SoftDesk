from rest_framework import serializers

from projects_api.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "issue",
            "author",
            "created_time",
        ]
