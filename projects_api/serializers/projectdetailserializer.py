from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers

from projects_api.models import Contributor, Project, choicesclass


class ProjectDetailSerializer(serializers.ModelSerializer):
    class UserContributorSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ["id"]

        def to_representation(self, instance):
            user = instance.user if isinstance(instance, Contributor) else instance
            return user.id

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
                permission=choicesclass.Permission.AUTHOR,
            )
            return instance
