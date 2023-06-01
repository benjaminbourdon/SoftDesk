from django.urls import include, path
from rest_framework import routers

from projects_api.views import ProjectViewset

router = routers.SimpleRouter()
router.register("projects", ProjectViewset, basename="project")

urlpatterns = [
    path("", include(router.urls)),
]
