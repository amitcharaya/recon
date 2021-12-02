from django.db import models

# Create your models here.
class AccountType(models.Model):
    type=models.CharField(max_length=250)
    def __str__(self):
        return self.type
class Account(models.Model):
    number=models.CharField(max_length=16)
    name=models.CharField(max_length=250)
    openingBalance=models.FloatField()
    date = models.DateField()
    accountType=models.ForeignKey(AccountType,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class TxnType(models.Model):
    type=models.CharField(max_length=26)

    def __str__(self):
        return self.type

class Transaction(models.Model):
    txnNo=models.CharField(max_length=25)
    account=models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    date=models.DateField()
    drTxn=models.FloatField()
    crTxn=models.FloatField()
    txnTpe=models.ForeignKey(TxnType,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.txnNo

