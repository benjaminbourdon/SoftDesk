from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission

from projects_api.models import Contributor


class IsContributorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = request.user

        try:
            contributor = obj.contributors.get(user=current_user)
        except ObjectDoesNotExist:
            return False

        if contributor.permission >= Contributor.Permission.CONTRIBUTOR:
            return True

        return False


class IsAuthorPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = request.user

        try:
            contributor = obj.contributors.get(user=current_user)
        except ObjectDoesNotExist:
            return False

        if contributor.permission >= Contributor.Permission.AUTHOR:
            return True

        return False
