from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested.routers import NestedSimpleRouter

from projects_api.views import (
    ProjectViewset,
    IssuesViewSet,
    CommentsViewSet,
    ContributorViewSet,
)

main_router = SimpleRouter()
main_router.register("projects", ProjectViewset, basename="project")

project_router = NestedSimpleRouter(main_router, "projects", lookup="project")
project_router.register("issues", IssuesViewSet, basename="issues-project")
project_router.register("users", ContributorViewSet, basename="contributors-project")

issue_router = NestedSimpleRouter(project_router, "issues", lookup="issue")
issue_router.register("comments", CommentsViewSet, basename="comments-issue-project")

urlpatterns = [
    path("auth/", include("projects_api.auth.urls")),
    path("", include(main_router.urls)),
    path("", include(project_router.urls)),
    path("", include(issue_router.urls)),
]
