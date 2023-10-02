from rest_framework import serializers
from .models import User


class CourseSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'
