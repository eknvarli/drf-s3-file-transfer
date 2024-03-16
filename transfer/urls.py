from rest_framework.routers import DefaultRouter
from django.urls import path, include
from transfer.views import FileViewSet

router = DefaultRouter()
router.register(r'files', FileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]