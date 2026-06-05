from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import ProjectViewset, ContributorViewset, IssueViewset, CommentViewset

router = DefaultRouter()
router.register("project", ProjectViewset, basename="project")
router.register("contributor", ContributorViewset, basename="contributor")
router.register("issue", IssueViewset, basename="issue")
router.register("comment", CommentViewset, basename="comment")

urlpatterns = [path("", include(router.urls))]
