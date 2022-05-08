from django.shortcuts import render
from rest_framework import viewsets
from django.db.models.functions import ExtractMonth
from .serializers import UtilitiesSerializer, MonthlyDueSerializer, DuePerTenantSerializer, MonthlyDuePerTenantSerializer
from .models import Utilities, DuePerTenant, MonthlyDuePerTenant
from rooms.models import RoomsAssign
from credits.models import Credit
from django.db.models import Sum, Count

# Create your views here.

class UtilitiesView(viewsets.ModelViewSet):
    serializer_class = UtilitiesSerializer
    queryset = Utilities.objects.all()

class MonthlyDueView(viewsets.ModelViewSet):
    serializer_class = MonthlyDueSerializer
    queryset = Utilities.objects.values('formonth', 'foryear').annotate(amount=Sum('amount'))

class TotalDuePerMonthView(viewsets.ModelViewSet):
    serializer_class = DuePerTenantSerializer
    #queryset = Utilities.objects.values('formonth', 'foryear').annotate(amount=Sum('amount'))
    #queryset2 = Credit.objects.values('formonth', 'foryear').annotate(cramount=Sum('cramount'))
    # is this possible:
    # queryset = queryset1 join queryset2
    queryset = DuePerTenant.objects.raw('SELECT id, formonth, foryear,SUM(amount) as amount from (SELECT expenses_utilities.id, expenses_utilities.formonth, expenses_utilities.foryear, SUM(expenses_utilities.amount) as amount FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT credits_credit.id, credits_credit.formonth, credits_credit.foryear, SUM(credits_credit.cramount) as amount FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear')
    # queryset = DuePerTenant.objects.raw('SELECT id, formonth, foryear,SUM(amount) from (SELECT SUM(expenses_utilities.amount) as amount, expenses_utilities.formonth, expenses_utilities.foryear, expenses_utilities.id FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT SUM(credits_credit.cramount) as amount, credits_credit.formonth, credits_credit.foryear, credits_credit.id FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear')
    # queryset = DuePerTenant.objects.raw('SELECT id, formonth, foryear, SUM(amount) from (SELECT SUM(expenses_utilities.amount) as amount, expenses_utilities.formonth, expenses_utilities.foryear FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT SUM(credits_credit.cramount) as amount, credits_credit.formonth, credits_credit.foryear FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear')

class MonthlyDuePerTenantView(viewsets.ModelViewSet):
    serializer_class = MonthlyDuePerTenantSerializer
    queryset = MonthlyDuePerTenant.objects.raw('select id, monthly_due, monthly_tenants, (monthly_due/monthly_tenants) as dues_perTenant, formonth, foryear from (select id, month, year, tenants, (@csum := @csum + tenants) as monthly_tenants from ( SELECT rooms_roomsassign.id, COUNT(DISTINCT(rooms_roomsassign.tenantid_id)) AS tenants, rooms_roomsassign.formonth AS month, rooms_roomsassign.foryear AS year FROM rooms_roomsassign WHERE rooms_roomsassign.date_end  IS NULL GROUP BY rooms_roomsassign.formonth, rooms_roomsassign.foryear) As temp JOIN (SELECT @csum:=0) AS temp2) as t JOIN (SELECT SUM(amount) as monthly_due, formonth, foryear from (SELECT SUM(expenses_utilities.amount) as amount, expenses_utilities.formonth, expenses_utilities.foryear FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT SUM(credits_credit.cramount) as amount, credits_credit.formonth, credits_credit.foryear FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear) as a ON t.month=a.formonth AND t.year=a.foryear')

