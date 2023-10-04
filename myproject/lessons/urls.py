from django.urls import path
from .views import LessonCreateView, LessonRetrieveView, LessonUpdateView, LessonDeleteView

urlpatterns = [
    path('lessons/', LessonCreateView.as_view(), name='lesson-create'),
    path('lessons/<int:pk>/', LessonRetrieveView.as_view(), name='lesson-retrieve'),
    path('lessons/<int:pk>/update/', LessonUpdateView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDeleteView.as_view(), name='lesson-delete'),
]