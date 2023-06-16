from rest_framework.viewsets import ModelViewSet

from projects_api.mixins import ProjectPartPermissionsMixin, NoPatchMixin
from projects_api.models import Issue
from projects_api.pagination import ListSetPagination
from projects_api.serializers import IssuesSerializer


class IssuesViewSet(NoPatchMixin, ProjectPartPermissionsMixin, ModelViewSet):
    serializer_class = IssuesSerializer
    pagination_class = ListSetPagination

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])
