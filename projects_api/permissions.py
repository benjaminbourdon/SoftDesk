from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

from projects_api.models import Contributor, choicesclass


class ForbidAny(BasePermission):
    def has_permission(self, request, view):
        return False


class IsContributorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = request.user

        try:
            contributor = obj.contributors.get(user=current_user)
        except ObjectDoesNotExist:
            return False

        if contributor.permission >= choicesclass.Permission.CONTRIBUTOR:
            return True

        return False


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = request.user

        if hasattr(obj, "author"):
            return obj.author == current_user

        try:
            contributor = obj.contributors.get(user=current_user)
        except ObjectDoesNotExist:
            return False
        return contributor.permission >= Contributor.Permission.AUTHOR
