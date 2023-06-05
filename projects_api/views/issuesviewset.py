from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects_api.models import Issue
from projects_api.pagination import ListSetPagination

# from projects_api.permissions import IsContributorPermission
from projects_api.serializers import IssuesSerializer


class IssuesViewSet(ModelViewSet):
    serializer_class = IssuesSerializer

    pagination_class = ListSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter(project=self.kwargs["project_pk"])
