from django.db import models
from django.utils.dates import MONTHS

# Create your models here.
UTILITY_TYPE = (
    ('PGE', 'PGE'),
    ('Water', 'Water'),
    ('TvCable','TV/Cable'),
    ('WIFI', 'WIFI'),
    ('Groceries', 'Groceries'),
    ('Other', 'Other')
)

YEAR = (
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
)

class Utilities(models.Model):
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')
    utname = models.CharField(max_length=10, choices=UTILITY_TYPE, default='PGE')
    accountid = models.CharField(max_length=25)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date_utcreated = models.DateField()
    date_due = models.DateField()
    utdescription = models.TextField(max_length=200)

    def __str__(self):
        return self.utname

class DuePerTenant(models.Model):
    id = models.IntegerField(primary_key=True)
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')
    amount = models.DecimalField(max_digits=6, decimal_places=2)

class MonthlyDuePerTenant(models.Model):
    id = models.IntegerField(primary_key=True)
    monthly_due = models.DecimalField(max_digits=6, decimal_places=2)
    monthly_tenants = models.IntegerField(blank=True, null=True)
    dues_perTenant = models.DecimalField(max_digits=6, decimal_places=2)
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')

class MonthlyTotal(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=10)
    rent = models.DecimalField(max_digits=6, decimal_places=2)
    utilities = models.DecimalField(max_digits=6, decimal_places=2)
    monthly_total = models.DecimalField(max_digits=6, decimal_places=2)
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')

