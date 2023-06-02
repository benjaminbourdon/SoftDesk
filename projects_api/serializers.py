from rest_framework import serializers

from projects_api.models import Project


class ProjectDetailSerializer(serializers.ModelSerializer):
    # class UserContributorSerializer(serializers.BaseSerializer):
    #     def to_representation(self, instance):
    #         return instance.user.username

    # contributors = UserContributorSerializer(many=True)
    # contributors = serializers.SlugRelatedField(
    #     many=True, read_only=True, slug_field="contributor_username"
    # )
    contributors = serializers.ListField(read_only=True, source="contributors_name")

    class Meta:
        model = Project
        fields = [
            "id",
            "title",
            "description",
            "type",
            "contributors",
            # "author_user_id",
        ]
        read_only_fields = ["id", "contributors"]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id",
            "title",
        ]
        read_only_fields = fields
