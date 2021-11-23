from django.db import models

# Create your models here.
class Account(models.Model):
    number=models.CharField(max_length=16)
    name=models.CharField(max_length=250)
    openingBalance=models.FloatField()

class Transactions(models.Model):
    #account=
    drTxn=models.FloatField()
    crTxn=models.FloatField()
    #txnTpe=

class TxnType(models.Model):
    type=models.CharField(max_length=26)
