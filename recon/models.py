from django.db import models


# Create your models here.
class AccountType(models.Model):
    type = models.CharField(max_length=250)

    def __str__(self):
        return self.type


class Account(models.Model):
    number = models.CharField(max_length=16)
    name = models.CharField(max_length=250)
    openingBalance = models.FloatField()
    date = models.DateField()
    accountType = models.ForeignKey(AccountType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class TxnType(models.Model):
    type = models.CharField(max_length=26)

    def __str__(self):
        return self.type


class Transaction(models.Model):
    txnNo = models.CharField(max_length=25)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    drTxn = models.FloatField()
    crTxn = models.FloatField()
    txnTpe = models.ForeignKey(TxnType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.txnNo


class ReconDate(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class Description_NTSL(models.Model):
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.description

class NTSL_Dispute_Adjustments(models.Model):
    description = models.CharField(max_length=256)
    ref_no=models.CharField(max_length=256)
    debit=models.FloatField()
    credit=models.FloatField()

    def __str__(self):
        return str(self.ref_no)

class NTSL(models.Model):
    class Meta:
        unique_together = (('date', 'cycle','description'),)
    cycle=models.CharField(max_length=2)
    date=models.DateField()
    description=models.ForeignKey(Description_NTSL,on_delete=models.SET_NULL,null=True)
    nooftxns=models.IntegerField()
    debit = models.FloatField()
    credit = models.FloatField()

    def __str__(self):
        return str(self.date)+" "+self.cycle +" "+self.description.description

class InwardOutward(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Status(models.Model):
    status=models.CharField(max_length=50)

    def __str__(self):
        return self.status

class TransactionCycle(models.Model):
    transactionCycle=models.CharField(max_length=50)

    def __str__(self):
        return self.transactionCycle

class TransactionType(models.Model):
    transactionType=models.CharField(max_length=50)

    def __str__(self):
        return self.transactionType

class Channel(models.Model):
    channel=models.CharField(max_length=50)

    def __str__(self):
        return self.channel

class RGCS(models.Model):
    date=models.DateField(null=True)
    cycle=models.CharField(max_length=1)
    productName=models.CharField(max_length=50)
    bankName=models.CharField(max_length=250)
    settlementBin=models.CharField(max_length=50)
    acqId=models.CharField(max_length=50)
    inwardOutward=models.ForeignKey(InwardOutward,on_delete=models.SET_NULL,null=True)
    status=models.ForeignKey(Status,on_delete=models.SET_NULL,null=True)
    transactionCycle=models.ForeignKey(TransactionCycle,on_delete=models.SET_NULL,null=True)
    transactionType=models.ForeignKey(TransactionType,on_delete=models.SET_NULL,null=True)
    channel=models.ForeignKey(Channel,on_delete=models.SET_NULL,null=True)
    txnCount=models.IntegerField(null=True)
    txnCCY=models.IntegerField(null=True)
    txnAmtDr=models.FloatField(null=True)
    txnAmtCr=models.FloatField(null=True)
    setCCY=models.IntegerField(null=True)
    setAmtDr=models.FloatField(null=True)
    setAmtCr=models.FloatField(null=True)
    intFeeAmtDr=models.FloatField(null=True)
    intFeeAmtCr=models.FloatField(null=True)
    memIncFeeAmtDr=models.FloatField(null=True)
    memIncFeeAmtCr = models.FloatField(null=True)
    customerCompensationDr=models.FloatField(null=True)
    customerCompensationCr = models.FloatField(null=True)
    othFeeAmtDr=models.FloatField(null=True)
    othFeeAmtCr = models.FloatField(null=True)
    othFeeGstDr = models.FloatField(null=True)
    othFeeGstCr = models.FloatField(null=True)
    finalSumCr=models.FloatField(null=True)
    finalSumDr = models.FloatField(null=True)
    finalNet=models.FloatField(null=True)

    def __str__(self):
        return str(self.date)+str(self.cycle)