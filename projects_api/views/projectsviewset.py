from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects_api.models import Project, Contributor
from projects_api.pagination import ListSetPagination
from projects_api.permissions import IsAuthorPermission, IsContributorPermission
from projects_api.serializers import ProjectDetailSerializer, ProjectListSerializer


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectDetailSerializer
    list_serializers_class = ProjectListSerializer

    pagination_class = ListSetPagination

    def get_queryset(self):
        return (
            Project.objects.prefetch_related("contributors__user")
            .filter(
                contributors__user=self.request.user,
                contributors__permission__gte=Contributor.Permission.CONTRIBUTOR,
            )
            .distinct()
        )

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializers_class
        return super().get_serializer_class()

    def get_permissions(self):
        if self.action in ("list", "create"):
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated, IsContributorPermission]
        else:
            self.permission_classes = [IsAuthenticated, IsAuthorPermission]
        return super().get_permissions()
