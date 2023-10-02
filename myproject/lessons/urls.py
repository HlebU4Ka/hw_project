from django.urls import path, include
from .views import LessonViewSet, LessonDetailViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]