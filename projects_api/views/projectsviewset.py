from rest_framework.viewsets import ModelViewSet

from projects_api.serializers import ProjectDetailSerializer, ProjectListSerializer
from projects_api.models import Project
from projects_api.pagination import ListSetPagination


class ProjectViewset(ModelViewSet):
    list_serializer_class = ProjectListSerializer
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.prefetch_related("contributors")
    pagination_class = ListSetPagination

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializer_class
        return super().get_serializer_class()
