from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

from projects_api.models import Contributor
from projects_api.pagination import ListSetPagination

from projects_api.serializers import (
    ContributorListSerializer,
    ContributorCreateSerializer,
)


class ContributorViewSet(
    GenericViewSet, CreateModelMixin, ListModelMixin, DestroyModelMixin
):
    serializer_class = ContributorCreateSerializer
    list_serializers_class = ContributorListSerializer

    pagination_class = ListSetPagination
    permission_classes = [IsAuthenticated]

    lookup_field = "user__id"
    lookup_url_kwarg = "pk"

    def get_queryset(self):
        return Contributor.objects.filter(project=self.kwargs["project_pk"]).order_by(
            "user"
        )

    def get_serializer_class(self):
        if self.action == "list":
            return self.list_serializers_class
        return super().get_serializer_class()
