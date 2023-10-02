from django.db import models
from myproject.users.models import User


# Create your models here.
class PaymentManager(models.Manager):
    def get_by_user(self, user_id):
        return self.filter(user_id=user_id)


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = None # Payment methods сделать
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateTimeField()
    course_of_lesson = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=[('cash', 'Наличные'), ('transfer', 'Перевод на счет')]
    )
    objects = PaymentManager()

    def __str__(self):
        return f"Оплачено {self.course_of_lesson} кем {self.user.email}"
