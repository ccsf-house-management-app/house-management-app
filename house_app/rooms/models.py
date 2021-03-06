from django.conf import settings
from django.db import models
from django.utils.dates import MONTHS
from users.models import UserInfo


YEAR = (
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
)

# Create your models here.

class Rooms(models.Model):
    roomId = models.CharField(blank=True, null=True, max_length=10)
    roomName = models.CharField(blank=True, null=True, max_length=25)
    roomDescription = models.CharField(blank=True, null=True, max_length=25)
    rent = models.DecimalField(blank=True, null=True, max_digits=6, decimal_places=2)
    capacity = models.IntegerField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.roomName


class RoomsAssign(models.Model):
    roomid = models.ForeignKey(Rooms, blank=True, null=True, on_delete=models.CASCADE)
    tenantid = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_transaction = models.DateField(auto_now=True)
    transactionId = models.CharField(blank=True, null=True, max_length=25)
    remarks = models.TextField(blank=True, null=True, max_length=200)
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')

    def __int__(self):
        return self.tenantid

class JoinRoom(models.Model):
    id=models.IntegerField(primary_key=True)
    roomid = models.ForeignKey(Rooms, blank=True, null=True, on_delete=models.CASCADE)
    tenantid = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    date_transaction = models.DateField(auto_now=True)
    transactionId = models.CharField(max_length=25,null=True)
    remarks = models.TextField(max_length=200, null=True)
    roomName = models.CharField(max_length=25, null=True)
    roomDescription = models.CharField(max_length=25, null=True)
    rent = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.IntegerField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    firstname = models.CharField(max_length=25, default='your first name')
    lastname = models.CharField(max_length=25, default='your last name')

class MonthlyTenant(models.Model):
    id = models.IntegerField(primary_key=True)
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')
    tenants = models.IntegerField(blank=True, null=True)
    monthly_tenants = models.IntegerField(blank=True, null=True)


