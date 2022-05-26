
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import AccountSerializer
from .models import Account
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

# Displays accounts for all tenants
class AccountView(viewsets.ModelViewSet):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

# Displays account view per tenant
class AccountDetailView(DetailView):
    template_name = 'accounts/account_detail.html'
    queryset = Account.objects.all()[0]

    def get_object(self):
        id_ = self.kwargs.get("user")
        return get_object_or_404(Account, user=id_)