from django.db import models

# Create your models here.

class UserInfo(models.Model):
    # userid = models.ForeignKey('auth.User', blank=True, null=True, on_delete=models.CASCADE)
    userid = models.OneToOneField('auth.User', blank=True, null=False, on_delete=models.CASCADE, primary_key=True)
    firstname = models.CharField(max_length=25)
    lastname  = models.CharField(max_length=10)
    birthdate = models.DateField()
    email  = models.EmailField(max_length=30)
    phone =models.CharField(max_length=10)
    date_created= models.DateField()

    def __str__(self):
        return self.firstname



