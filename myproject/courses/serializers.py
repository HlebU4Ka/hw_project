from rest_framework import serializers
from .models import Course
from myproject.lessons.serializers import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'preview',
                  'description', 'num_lessons')

        def get_num_lessons(self, obj):
            return obj.lesson_set.count()
