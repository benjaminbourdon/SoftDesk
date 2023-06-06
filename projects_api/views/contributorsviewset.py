from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects_api.models import Contributor
from projects_api.pagination import ListSetPagination

# from projects_api.permissions import IsContributorPermission
from projects_api.serializers import ContributorSerializer


class ContributorViewSet(ModelViewSet):
    serializer_class = ContributorSerializer

    pagination_class = ListSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"]).order_by(
            "user"
        )
