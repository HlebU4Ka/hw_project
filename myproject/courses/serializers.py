from rest_framework import serializers
from myproject.lessons.serializers import LessonSerializer
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'preview', 'description', 'num_lessons')

    def get_num_lessons(self, obj):
        return obj.lesson_set.count()
