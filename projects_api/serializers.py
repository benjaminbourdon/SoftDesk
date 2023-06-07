from django.db import transaction
from rest_framework import serializers

from projects_api.models import Comment, Contributor, Issue, Project


class ProjectDetailSerializer(serializers.ModelSerializer):
    class UserContributorSerializer(serializers.ModelSerializer):
        def to_representation(self, instance):
            return instance.user.id

    contributors_id = UserContributorSerializer(
        source="contributors", many=True, read_only=True
    )
    author_user_id = UserContributorSerializer(source="author", read_only=True)
    # author_user_id = serializers.PrimaryKeyRelatedField(source="author", read_only=True)

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "type",
            "author_user_id",
            "contributors_id",
        ]

    def create(self, validated_data):
        with transaction.atomic():
            instance = super().create(validated_data)
            Contributor.objects.create(
                project=instance,
                user=self.context["request"].user,
                permission=Contributor.Permission.AUTHOR,
            )
            return instance


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
        ]
        read_only_fields = fields


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


class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = ["user"]

    def to_representation(self, instance):
        return {
            "id": instance.user.id,
            "username": instance.user.username,
        }
