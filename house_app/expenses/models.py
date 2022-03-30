from django.db import models
from django.utils.dates import MONTHS

# Create your models here.
UTILITY_TYPE = (
    ('a', 'PGE'),
    ('b', 'Water'),
    ('c','TV/Cable'),
    ('d', 'WIFI'),
    ('e', 'Groceries'),
    ('f', 'Other')
)

YEAR = (
    ('a','2022'),
    ('b','2023'),
    ('c','2024'),
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

