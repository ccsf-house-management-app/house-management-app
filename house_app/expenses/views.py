from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UtilitiesSerializer
from .models import Utilities

# Create your views here.

class UtilitiesView(viewsets.ModelViewSet):
    serializer_class = UtilitiesSerializer
    queryset = Utilities.objects.all()
