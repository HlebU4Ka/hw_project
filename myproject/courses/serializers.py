from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = Course
        fields = '__all__'
