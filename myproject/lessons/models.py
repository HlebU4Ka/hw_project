from django.db import models


class LessonManager(models.Manager):
    def get_lessons_by_title(self, title):
        return self.filter(title__icontains=title)

# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(up_to_date='lesson_preview')
    video_link = models.URLField()

    objects = LessonManager()

    def __str__(self):
        return self.title
