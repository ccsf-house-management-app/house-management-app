from django.shortcuts import render
from rest_framework import viewsets
from django.db.models.functions import ExtractMonth
from .serializers import UtilitiesSerializer, MonthlyDueSerializer, DuePerTenantSerializer, MonthlyDuePerTenantSerializer, MonthlyTotalSerializer
from .models import Utilities, DuePerTenant, MonthlyDuePerTenant, MonthlyTotal
from rooms.models import RoomsAssign, Rooms, MonthlyTenant
from credits.models import Credit
from users.models import UserInfo
from django.db.models import Sum, Count
from itertools import chain
import requests
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

# Create your views here.

class UtilitiesView(viewsets.ModelViewSet):
    serializer_class = UtilitiesSerializer
    queryset = Utilities.objects.all()

# Displays monthly dues from the Utilities model
class MonthlyDueView(viewsets.ModelViewSet):
    serializer_class = MonthlyDueSerializer
    queryset = Utilities.objects.values('formonth', 'foryear').annotate(amount=Sum('amount'))

# Displays the combined monthly dues from both the Utilities model and Credits model
class TotalDuePerMonthView(viewsets.ModelViewSet):
    serializer_class = DuePerTenantSerializer
    queryset = DuePerTenant.objects.raw('SELECT id, formonth, foryear,SUM(amount) as amount from (SELECT expenses_utilities.id, expenses_utilities.formonth, expenses_utilities.foryear, SUM(expenses_utilities.amount) as amount FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT credits_credit.id, credits_credit.formonth, credits_credit.foryear, SUM(credits_credit.cramount) as amount FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear')

# Displays the combined monthly dues and Dues per Tenant for each month
class MonthlyDuePerTenantView(viewsets.ModelViewSet):
    serializer_class = MonthlyDuePerTenantSerializer
    queryset = MonthlyDuePerTenant.objects.raw('select id, monthly_due, monthly_tenants, (monthly_due/monthly_tenants) as dues_perTenant, formonth, foryear from (select id, month, year, tenants, (@csum := @csum + tenants) as monthly_tenants from ( SELECT rooms_roomsassign.id, COUNT(DISTINCT(rooms_roomsassign.tenantid_id)) AS tenants, rooms_roomsassign.formonth AS month, rooms_roomsassign.foryear AS year FROM rooms_roomsassign WHERE rooms_roomsassign.date_end  IS NULL GROUP BY rooms_roomsassign.formonth, rooms_roomsassign.foryear) As temp JOIN (SELECT @csum:=0) AS temp2) as t JOIN (SELECT SUM(amount) as monthly_due, formonth, foryear from (SELECT SUM(expenses_utilities.amount) as amount, expenses_utilities.formonth, expenses_utilities.foryear FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT SUM(credits_credit.cramount) as amount, credits_credit.formonth, credits_credit.foryear FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear) as a ON t.month=a.formonth AND t.year=a.foryear')

class MonthlyTotalView(viewsets.ModelViewSet):
    serializer_class = MonthlyTotalSerializer
    queryset = MonthlyTotal.objects.raw('select rooms_roomsassign.tenantid_id as id, users_userinfo.firstname as firstname, users_userinfo.lastname as lastname, rooms_rooms.rent as rent, newt.dues_perTenant as utilities, (rooms_rooms.rent+newt.dues_perTenant) as monthly_total,newt.formonth as formonth, newt.foryear as foryear from rooms_roomsassign JOIN rooms_rooms on rooms_roomsassign.roomid_id=rooms_rooms.id JOIN(select id, monthly_due, monthly_tenants, (monthly_due/monthly_tenants) as dues_perTenant, formonth, foryear from (select id, month, year, tenants, (@csum := @csum + tenants) as monthly_tenants from ( SELECT rooms_roomsassign.id, COUNT(DISTINCT(rooms_roomsassign.tenantid_id)) AS tenants, rooms_roomsassign.formonth AS month, rooms_roomsassign.foryear AS year FROM rooms_roomsassign WHERE rooms_roomsassign.date_end  IS NULL GROUP BY rooms_roomsassign.formonth, rooms_roomsassign.foryear) As temp JOIN (SELECT @csum:=0) AS temp2) as t JOIN (SELECT SUM(amount) as monthly_due, formonth, foryear from (SELECT SUM(expenses_utilities.amount) as amount, expenses_utilities.formonth, expenses_utilities.foryear FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT SUM(credits_credit.cramount) as amount, credits_credit.formonth, credits_credit.foryear FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear) as a ON t.month=a.formonth AND t.year=a.foryear) as newt JOIN users_userinfo ON users_userinfo.userid_id=rooms_roomsassign.tenantid_id WHERE MONTH(rooms_roomsassign.date_start) <= newt.formonth')

class TotalDuePerMonthDetailView(ListView):
    template_name = 'expenses/utility_detail.html'
    queryset = MonthlyDuePerTenant.objects.raw('select id, monthly_due, monthly_tenants, (monthly_due/monthly_tenants) as dues_perTenant, formonth, foryear from (select id, month, year, tenants, (@csum := @csum + tenants) as monthly_tenants from ( SELECT rooms_roomsassign.id, COUNT(DISTINCT(rooms_roomsassign.tenantid_id)) AS tenants, rooms_roomsassign.formonth AS month, rooms_roomsassign.foryear AS year FROM rooms_roomsassign WHERE rooms_roomsassign.date_end  IS NULL GROUP BY rooms_roomsassign.formonth, rooms_roomsassign.foryear) As temp JOIN (SELECT @csum:=0) AS temp2) as t JOIN (SELECT SUM(amount) as monthly_due, formonth, foryear from (SELECT SUM(expenses_utilities.amount) as amount, expenses_utilities.formonth, expenses_utilities.foryear FROM expenses_utilities GROUP BY expenses_utilities.formonth, expenses_utilities.foryear UNION SELECT SUM(credits_credit.cramount) as amount, credits_credit.formonth, credits_credit.foryear FROM credits_credit GROUP BY credits_credit.formonth, credits_credit.foryear) as temp GROUP BY formonth, foryear) as a ON t.month=a.formonth AND t.year=a.foryear')

def monthlydues(request):
    displaytable=requests.get('http://127.0.0.1:8000/api/monthlytotal/')
    result=displaytable.json()
    return render(request,"expenses/monthlytotal.html", {"MonthlyTotal":result})
