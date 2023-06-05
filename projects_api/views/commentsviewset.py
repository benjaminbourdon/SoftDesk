from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from projects_api.models import Comment
from projects_api.pagination import ListSetPagination

# from projects_api.permissions import IsContributorPermission
from projects_api.serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    pagination_class = ListSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(
            issue__project=self.kwargs["project_pk"], issue=self.kwargs["issue_pk"]
        )
