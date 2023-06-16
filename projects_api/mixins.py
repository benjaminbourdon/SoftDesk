from rest_framework.permissions import IsAuthenticated
from projects_api.permissions import (
    IsContributorPermission,
    IsAuthorPermission,
    ForbidAny,
)


class ProjectPartPermissionsMixin:
    """Mixin for class view representing parts of projects like issues and comments"""

    def get_permissions(self):
        if self.action in ("list", "retrieve", "create"):
            self.permission_classes = [IsAuthenticated, IsContributorPermission]
        elif self.action == "partial_update":
            self.permission_classes = [ForbidAny]
        else:
            self.permission_classes = [IsAuthenticated, IsAuthorPermission]
        return [permission() for permission in self.permission_classes]


class NoPatchMixin:
    def __init__(self, *args, **kwargs) -> None:
        if "patch" in self.http_method_names:
            self.http_method_names.remove("patch")
        super().__init__(*args, **kwargs)
