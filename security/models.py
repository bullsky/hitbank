from django.db import models
from login.models import *
from register.models import *
from transfer.models import *
# Create your models here.


class EncryptionAlgorithm(models.Model):
    id = models.AutoField(primary_key=True)
    pk_algo = models.CharField(max_length=8)
    user_pkey = models.CharField(max_length=64)
    bank_pkey = models.CharField(max_length=64)
    bank_skey = models.CharField(max_length=64)
    sk_algo = models.CharField(max_length=8)
    sym_key = models.CharField(max_length=64)

    def __unicode__(self):
        return self.id


class LoginAudit(models.Model):
    seq = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    password = models.CharField(max_length=64)
    user_ip = models.GenericIPAddressField()
    Algorithm = models.ForeignKey(EncryptionAlgorithm, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.seq


class BusinessAudit(models.Model):
    seq = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    serial = models.ForeignKey(Flow, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    password = models.CharField(max_length=64)
    paycode = models.CharField(max_length=6)
    user_ip = models.GenericIPAddressField()
    Algorithm = models.ForeignKey(EncryptionAlgorithm, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.seq


class PayAudit(models.Model):
    seq = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    serial = models.ForeignKey(Flow, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    password = models.CharField(max_length=64)
    paycode = models.CharField(max_length=6)
    order_hash = models.CharField(max_length=64)
    pay_info = models.CharField(max_length=128)
    double_sign = models.CharField(max_length=64)
    Algorithm = models.ForeignKey(EncryptionAlgorithm, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.seq
