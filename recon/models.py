from django.db import models

# Create your models here.
class Account(models.Model):
    number=models.CharField(max_length=16)
    name=models.CharField(max_length=250)
    openingBalance=models.FloatField()
    date = models.DateField()
    def __str__(self):
        return self.name

class Transactions(models.Model):
    txnNo=models.CharField(max_length=25)
    #account=
    date:models.DateField()
    drTxn=models.FloatField()
    crTxn=models.FloatField()
    #txnTpe=

    def __str__(self):
        return self.txnNo

class TxnType(models.Model):
    type=models.CharField(max_length=26)

    def __str__(self):
        return self.type