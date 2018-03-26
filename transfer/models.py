from django.db import models
from login.models import *
from register.models import *
# Create your models here.


class Flow(models.Model):
    serial = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    s_account = models.CharField(max_length=16)
    s_bankcard = models.CharField(max_length=19)
    #s_account = models.ManyToManyField(Account)
    #s_bankcard = models.ManyToManyField(BankCard)
    currency = models.CharField(max_length=4)
    amount = models.BigIntegerField(default=0)
    balance = models.BigIntegerField(default=0)
    type = models.CharField(max_length=8)
    target_web = models.URLField()
    d_account = models.CharField(max_length=16)
    d_bankcard = models.CharField(max_length=19)
    #d_account = models.ManyToManyField(Account)
    #d_bankcard = models.ManyToManyField(BankCard)

    def __unicode__(self):
        return self.serial
