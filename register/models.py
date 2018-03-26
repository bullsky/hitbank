from django.db import models

# Create your models here.


class Identity(models.Model):
    name = models.CharField(max_length=32)
    id_card_num = models.CharField(max_length=18, primary_key=True)
    birthday = models.DateField()
    age = models.CharField(max_length=3)
    address = models.CharField(max_length=32)

    def __unicode__(self):
        return self.id_card_num


class BankCard(models.Model):
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)
    phone_num = models.CharField(max_length=11)
    bank_card_num = models.CharField(max_length=19, primary_key=True)
    paycode = models.CharField(max_length=6)
    balance = models.BigIntegerField(default=0)
    currency = models.CharField(max_length=4)

    def __unicode__(self):
        return self.bank_card_num

