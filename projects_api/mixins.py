from rest_framework.permissions import IsAuthenticated
from projects_api.permissions import IsContributorPermission, IsAuthorPermission


class ProjectPartPermissionsMixin:
    """Mixin for class view representing parts of projects like issues and comments"""

    def get_permissions(self):
        if self.action in ("list", "retrieve", "create"):
            self.permission_classes = [IsAuthenticated, IsContributorPermission]
        else:
            self.permission_classes = [IsAuthenticated, IsAuthorPermission]
        return [permission() for permission in self.permission_classes]
