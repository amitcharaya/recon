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
    txnNo = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    date = models.DateField()
    drTxn = models.FloatField()
    crTxn = models.FloatField()
    txnType = models.ForeignKey(TxnType, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-txnNo']
    def __str__(self):
        return str(self.txnNo)+" "+str(self.date) +" "+self.account.name +" "+str(self.drTxn)+" "+str(self.crTxn)


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
    status=models.CharField(max_length=10)
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
    class Meta:
        unique_together = (('date', 'cycle', 'inwardOutward','status','transactionCycle','transactionType','channel'),)
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
    postingstatus=models.CharField(max_length=10)
    def __str__(self):
        return str(self.date)+str(self.cycle)


class TipandSurcharge(models.Model):
    class Meta:
        unique_together = (('date', 'cycle'),)
    date=models.DateField()
    cycle=models.CharField(max_length=5)
    finalAmount =models.FloatField()
    status=models.CharField(max_length=10)

    def __str__(self):
        return str(self.date)+" "+ str(self.finalAmount)


class PendingEntries(models.Model):
    date=models.DateField()
    debitAmount = models.FloatField()
    creditAmount = models.FloatField()
    adjustmentDate = models.DateField(null=True,blank=True)
    description = models.CharField(max_length=100)
    status=models.CharField(max_length=10)
    def __str__(self):
        return str(self.date) + " " + str(self.debitAmount) + " " +str(self.creditAmount)+" "+str(self.description)

