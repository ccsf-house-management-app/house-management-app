from django.conf import settings
from django.db import models
from django.utils.dates import MONTHS

# Create your models here.
BILL_TYPE = (
    ('All', 'All'),
    ('Rent', 'Rent'),
    ('Utilities','Utilities'),
    ('Deposit', 'Deposit'),
    ('Others','Others'),

)

YEAR = (
    ('a','2022'),
    ('b','2023'),
    ('c','2024'),
)

class Account(models.Model):
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True, on_delete=models.CASCADE)
    bill_type = models.CharField(max_length=10, choices=BILL_TYPE, default='All')
    accountid = models.CharField(max_length=25)
    paidamount = models.DecimalField(max_digits=6, decimal_places=2)
    date_paid = models.DateField()
    description = models.TextField(max_length=200, blank=True, null=True,)

    def __int__(self):
        return self.user

