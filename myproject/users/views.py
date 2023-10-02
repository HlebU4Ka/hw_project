from rest_framework import viewsets
from .models import User
from .serializers import CourseSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CourseSerializer
