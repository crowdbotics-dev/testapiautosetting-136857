from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors136857ViewSet

router = DefaultRouter()
router.register(
    "testconnectors136857", Testconnectors136857ViewSet, basename="testconnectors136857"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
