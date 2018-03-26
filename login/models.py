from django.db import models

# Create your models here.


class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=8)
    passwd = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Account(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    type = models.CharField(max_length=8)
    passwd = models.CharField(max_length=64)
    regist_data = models.DateField()
    status = models.CharField(max_length=8)

    def __unicode__(self):
        return self.uid