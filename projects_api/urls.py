from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from projects_api.views import ProjectViewset, IssuesViewSet, CommentsViewSet

router = SimpleRouter()
router.register("projects", ProjectViewset, basename="project")

project_router = NestedSimpleRouter(router, "projects", lookup="project")
project_router.register("issues", IssuesViewSet, basename="issues-project")

comment_route = NestedSimpleRouter(project_router, "issues", lookup="issue")
comment_route.register("comments", CommentsViewSet, basename="comments-issue-project")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(project_router.urls)),
    path("", include(comment_route.urls)),
]
