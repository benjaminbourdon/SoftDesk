# Inspired by
# https://medium.com/django-rest/django-rest-framework-login-and-register-user-fd91cf6029d5

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.db import transaction
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
            "email",
            "first_name",
            "last_name",
        ]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Les mots de passe ne sont pas identiques."}
            )
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            user = User.objects.create_user(
                username=validated_data["username"],
                password=validated_data["password"],
            )
            user.email = validated_data["email"] if "email" in validated_data else ""
            user.first_name = (
                validated_data["first_name"] if "first_name" in validated_data else ""
            )
            user.last_name = (
                validated_data["last_name"] if "last_name" in validated_data else ""
            )
            user.save()
            return user
