from django.db import models

avatars_settings = {
    'null': True,
    'blank': True

}


class UserManager(models.Manager):
    def get_users_from_city(self, city):
        return self.filter(city__iexact=city)

    def get_users_with_avatar(self):
        return self.exclude(avatar='')


# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=200, db_index=True)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='images/', **avatars_settings)

    objects = UserManager()

    def __str__(self):
        return self.email
