import django_filters
from .models import Payment


class PaymentFilter(django_filters.FilterSet):
    # Фильтр по дате оплаты
    min_payment_date = django_filters.DateFilter(field_name='payment_date', lookup_expr='gte')
    max_payment_date = django_filters.DateFilter(field_name='payment_date', lookup_expr='lte')

    # Фильтр по курсу или уроку
    course_or_lesson = django_filters.CharFilter(field_name='course_or_lesson', lookup_expr='contains')

    # Фильтр по способу оплаты
    payment_method = django_filters.ChoiceFilter(field_name='payment_method', choices=Payment.PAYMENT_METHOD_CHOICES)

    class Meta:
        model = Payment
        fields = []
