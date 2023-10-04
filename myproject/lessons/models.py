from django.db import models

avatars_settings = {
    'null': True,
    'blank': True

}


class LessonManager(models.Manager):
    def get_lessons_by_title(self, title):
        return self.filter(title__icontains=title)


# Create your models here.
class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview = models.ImageField(upload_to='images/', **avatars_settings)
    video_link = models.URLField()

    objects = LessonManager()

    def __str__(self):
        return self.title
