"""Urls of /api app."""
from api.views import (
    ApplicationViewSetBasicAuth,
    ApplicationViewSetTokenAuth,
    GenerateNewKeyBasicAuth,
)
from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"apps", ApplicationViewSetBasicAuth)
router.register(r"test", ApplicationViewSetTokenAuth)

urlpatterns = [
    url(r"new-key", GenerateNewKeyBasicAuth.as_view()),
    url(r"^", include(router.urls)),
]
