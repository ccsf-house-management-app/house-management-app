from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CreditSerializer, OtherCreditSerializer
from .models import Credit
from django.db.models import Sum, Count

# Create your views here.

class CreditView(viewsets.ModelViewSet):
    serializer_class = CreditSerializer
    queryset = Credit.objects.all()

class OtherCreditView(viewsets.ModelViewSet):
    serializer_class = OtherCreditSerializer
    queryset = Credit.objects.values('formonth', 'foryear').annotate(cramount=Sum('cramount'))