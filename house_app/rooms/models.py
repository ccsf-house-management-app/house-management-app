from django.db import models

from users.models import UserInfo

# Create your models here.

class Rooms(models.Model):
    roomId = models.CharField(blank=True, null=True, max_length=10)
    roomName = models.CharField(max_length=25)
    roomDescription = models.CharField(max_length=25)
    rent = models.DecimalField(max_digits=6, decimal_places=2)
    capacity = models.IntegerField(blank=True, null=True)
    date_created = models.DateField()

    def __str__(self):
        return self.roomName


class RoomsAssign(models.Model):
    roomid = models.ForeignKey(Rooms, blank=True, null=True, on_delete=models.CASCADE)
    tenantid = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    date_transaction = models.DateField(auto_now=True)
    transactionId = models.CharField(max_length=25)
    remarks = models.TextField(max_length=200)

    def __int__(self):
        return self.tenantid

    # def get_absolute_url(self):
    #     return reverse("room-detail", kwargs={"id": seld.id})