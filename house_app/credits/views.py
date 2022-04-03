from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CreditSerializer
from .models import Credit

# Create your views here.

class CreditView(viewsets.ModelViewSet):
    serializer_class = CreditSerializer
    queryset = Credit.objects.all()
