from django.conf import settings
from django.db import models
from django.utils.dates import MONTHS
from django.contrib.auth import get_user_model

# Create your models here.
CREDIT_TYPE= (
    ('Chores', 'Chores'),
    ('Groceries', 'Groceries'),
    ('Other','Other')
)

YEAR = (
    ('2022','2022'),
    ('2023','2023'),
    ('2024','2024'),
)

class Credit(models.Model):
    User = get_user_model()

    # cruserid = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
    # cruserid = models.ForeignKey(settings.AUTH_USER_MODEL,
    #                              blank=True, null=True, on_delete=models.CASCADE)
    cruserid = models.ForeignKey(User,
                             blank=True, null=True, on_delete=models.CASCADE)
    formonth = models.IntegerField(blank=True, null=True, choices=MONTHS.items())
    foryear = models.CharField(blank=True, null=True, choices=YEAR, max_length=4, default='2022')
    crname = models.CharField(max_length=10, choices=CREDIT_TYPE, default='Chores')
    cracccount = models.CharField(blank=True, null=True, max_length=25)
    cramount = models.DecimalField(max_digits=6, decimal_places=2)
    date_cr = models.DateField()
    date_done = models.DateField()
    crdescription = models.TextField(max_length=200)

    def __int__(self):
        return self.cruserid


