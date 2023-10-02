from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer


# Create your views here.

class LessonViewSet(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
