from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register("projects")
# router.register("issues")
# router.register("comments")

urlpatterns = [path("", include(router.urls))]
