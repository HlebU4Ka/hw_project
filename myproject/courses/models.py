from django.db import models


class CourseManager(models.Manager):
    def get_courses_by_description(self, description):
        return self.filter(description__icontains=description)


class Course(models.Model):
    title = models.CharField(max_length=255)
    preview = models.ImageField(upload_to="courses_preview")
    description = models.TextField(blank=True)

    objects = CourseManager()

    def __str__(self):
        return self.title
