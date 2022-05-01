from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UtilitiesSerializer, MonthlyDueSerializer
from .models import Utilities
from django.db.models import Sum

# Create your views here.

class UtilitiesView(viewsets.ModelViewSet):
    serializer_class = UtilitiesSerializer
    queryset = Utilities.objects.all()

class MonthlyDueView(viewsets.ModelViewSet):
    serializer_class = MonthlyDueSerializer
    queryset = Utilities.objects.values('formonth', 'foryear').annotate(amount=Sum('amount'))
