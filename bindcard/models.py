from django.db import models
from login.models import *
from register.models import *
# Create your models here.


class UserCard(models.Model):
    uid = models.ForeignKey(Account, on_delete=models.CASCADE)
    bank_card_num = models.ForeignKey(BankCard, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.uid