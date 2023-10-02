from rest_framework import generics
from django_filters import rest_framework as django_filters
from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter


class PaymentListView(generics.ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterer_class = PaymentFilter


class PaymentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
