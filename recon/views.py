from django.contrib import messages
import pandas as pd
import xml.dom.minidom
from datetime import timedelta
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Account,Transaction,AccountType,TxnType,ReconDate,NTSL,NTSL_Dispute_Adjustments,Description_NTSL,InwardOutward,Status,TransactionType,TransactionCycle,Channel,RGCS,TipandSurcharge,PendingEntries
from .forms import AccountTypeForm,AccountForm,TransactionForm,TxnTypeForm,ReconDateFrom,UploadFileForm,UploadXMLFileForm,PendingEntryForm,UploadRGCSFileForm1
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Sum
from django.templatetags.static import static
from django.conf import settings
import os
import xlrd
import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    transactions = Transaction.objects.all()
    accounts=Account.objects.all()

    context={'accounts':accounts,'transactions':transactions}
    return render(request,'home.html',context)


def logoutuser(request):
    logout(request)
    return redirect('login')

def loginpage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password = request.POST.get('password')
        try:
            user=User.objects.get(username=username)

        except:
            messages.error(request, 'User does not exist')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password incorrect')


    context = {}
    return render(request, 'recon/login.html', context)

@login_required
def accounts(request):

    accounts=Account.objects.all()

    context={'accounts':accounts}

    return render(request,'recon/accounts.html',context)

@login_required
def pendingEntries(request):

    entries=PendingEntries.objects.all()

    context={'entries':entries}

    return render(request,'recon/pendingEntries.html',context)

@login_required
def pendingEntriesDetail(request):
    cldate=ReconDate.objects.all()
    entries=PendingEntries.objects.filter(
        Q(status="Pending")&
        Q(date__lte=cldate[0].date)
    )

    context={'entries':entries}

    return render(request,'recon/pendingEntries.html',context)

@login_required
def accounttypes(request):

    accounttypes = AccountType.objects.all()

    context = {'accounttypes': accounttypes}
    return render(request, 'recon/account_types.html', context)

@login_required
def transactions(request):

    transactions = Transaction.objects.all()

    context = {'transactions': transactions}
    return render(request, 'recon/transactions.html', context)

@login_required
def txntypes(request):

    txntypes = TxnType.objects.all()

    context = {'txntypes': txntypes}
    return render(request, 'recon/transaction_types.html', context)

@login_required
def createAccountTYpe(request):
    accounttypes = AccountType.objects.all()


    form=AccountTypeForm()
    if request.method=='POST':
        form=AccountTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form,'accounttypes': accounttypes}
    return render(request, 'recon/account_type_form.html', context)

@login_required
def createPendingEntry(request):
    pendingEntries = PendingEntries.objects.all()


    form=PendingEntryForm()
    if request.method=='POST':
        form=PendingEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form,'entries': pendingEntries}
    return render(request, 'recon/pending_entries_form.html', context)
@login_required
def createAccount(request):
    accounts = Account.objects.all()


    form=AccountForm()
    if request.method=='POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form,'accounts': accounts}
    return render(request,'recon/account_form.html',context)
@login_required
def deleteAccount(request,pk):
    account = Account.objects.get(id=pk)
    if request.method=='POST':
        account.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':account})
@login_required
def deleteAccounttype(request,pk):
    accounttype = AccountType.objects.get(id=pk)
    if request.method=='POST':
        accounttype.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':accounttype})
@login_required
def deleteTransaction(request,pk):
    transaction = Transaction.objects.get(txnNo=pk)
    if request.method=='POST':
        transaction.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':transaction})


@login_required
def updateAccount(request,pk):
    account= Account.objects.get(id=pk)
    form = AccountForm(instance=account)
    if request.method=='POST':
        form=AccountForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'recon/account_form.html', context)
@login_required
def deleteEntry(request,pk):
    entry = PendingEntries.objects.get(id=pk)
    if request.method=='POST':
        entry.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':entry})


@login_required
def updateEntry(request,pk):
    entry= PendingEntries.objects.get(id=pk)
    form = PendingEntryForm(instance=entry)
    if request.method=='POST':
        form=PendingEntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'recon/pending_entries_form.html', context)
@login_required
def updateAccounttype(request,pk):
    account= AccountType.objects.get(id=pk)
    form = AccountTypeForm(instance=account)
    if request.method=='POST':
        form=AccountTypeForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'recon/account_type_form.html', context)
@login_required
def updateTransaction(request,pk):
    transaction= Transaction.objects.get(txnNo=pk)
    form = TransactionForm(instance=transaction)
    if request.method=='POST':
        form=TransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'recon/transaction_form.html', context)


@login_required
def createTransaction(request):
    transactions = Transaction.objects.all()


    form=TransactionForm()
    if request.method=='POST':
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create-transaction')
    context={'form':form,'transactions': transactions}
    return render(request,'recon/transaction_form.html',context)
@login_required
def createTxntype(request):
    txntypes = TxnType.objects.all()


    form=TxnTypeForm()
    if request.method=='POST':
        form=TxnTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form,'txntypes': txntypes}
    return render(request,'recon/txntype_form.html',context)
@login_required
def updateTxnType(request,pk):
    txntype= TxnType.objects.get(id=pk)
    form = TxnTypeForm(instance=txntype)
    if request.method=='POST':
        form=TxnTypeForm(request.POST,instance=txntype)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'recon/txntype_form.html', context)

@login_required
def deleteTxnType(request,pk):
    txntype = TxnType.objects.get(id=pk)
    if request.method=='POST':
        txntype.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':txntype})
@login_required
def createRecondate(request):
    try:
        recondate=ReconDate.objects.all()[0]
        form = ReconDateFrom(instance=recondate)
    except ReconDate.DoesNotExist:
        form = ReconDateFrom()

    if request.method=='POST':
        try:
            form=ReconDateFrom(request.POST,instance=recondate)
        except UnboundLocalError:
            form = ReconDateFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'recon/recondate_form.html',context)

def MirrorCrEntriesDuringDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Mirror Account')
    account = Account.objects.filter(accountType=accountType[0])
    txnTypeobj=TxnType.objects.filter(type="System")
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date,txnType__in=txnTypeobj).aggregate(Sum('crTxn'))
    if transactions['crTxn__sum']==None:
        transactions['crTxn__sum']=0
    return transactions['crTxn__sum']

def MirrorDrEntriesDuringDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Mirror Account')
    txnTypeobj = TxnType.objects.filter(type="System")
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date,txnType__in=txnTypeobj).aggregate(Sum('drTxn'))
    if transactions['drTxn__sum']==None:
        transactions['drTxn__sum']=0
    return transactions['drTxn__sum']

def IssuerDrEntriesDuringDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Issuer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('drTxn'))
    if transactions['drTxn__sum']==None:
        transactions['drTxn__sum']=0
    return transactions['drTxn__sum']

def IssuerCrEntriesDuringDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Issuer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('crTxn'))
    if transactions['crTxn__sum']==None:
        transactions['crTxn__sum']=0
    return transactions['crTxn__sum']

def AcquirerDrEntriesDuringDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Acquirer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('drTxn'))
    if transactions['drTxn__sum']==None:
        transactions['drTxn__sum']=0
    return transactions['drTxn__sum']



def AcquirerCrEntriesDuringDay():
    recondate = ReconDate.objects.all()[0]
    accountType = AccountType.objects.filter(type='Acquirer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions = Transaction.objects.filter(account=account[0], date=recondate.date).aggregate(Sum('crTxn'))
    if transactions['crTxn__sum']==None:
        transactions['crTxn__sum']=0
    return transactions['crTxn__sum']

def AcquirerEntriesDuringPrvDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Acquirer Account')
    account = Account.objects.filter(accountType=accountType[0])
    drtransactions=Transaction.objects.filter(account=account[0],date=recondate.date-timedelta(hours=24)).aggregate(Sum('drTxn'))
    crtransactions = Transaction.objects.filter(account=account[0], date=recondate.date - timedelta(hours=24)).aggregate(Sum('crTxn'))

    if drtransactions['drTxn__sum']==None:
        drtransactions['drTxn__sum']=0
    if crtransactions['crTxn__sum']==None:
        crtransactions['crTxn__sum']=0
    return drtransactions['drTxn__sum']-crtransactions['crTxn__sum']

def IssuerEntriesDuringPrvDay():
    recondate=ReconDate.objects.all()[0]
    accountType=AccountType.objects.filter(type='Issuer Account')
    account = Account.objects.filter(accountType=accountType[0])
    drtransactions=Transaction.objects.filter(account=account[0],date=recondate.date-timedelta(hours=24)).aggregate(Sum('drTxn'))
    crtransactions = Transaction.objects.filter(account=account[0], date=recondate.date - timedelta(hours=24)).aggregate(Sum('crTxn'))

    if drtransactions['drTxn__sum']==None:
        drtransactions['drTxn__sum']=0
    if crtransactions['crTxn__sum']==None:
        crtransactions['crTxn__sum']=0
    return crtransactions['crTxn__sum']-drtransactions['drTxn__sum']
@login_required
def ReconDashboard(request):
    acq=MirrorDrEntriesDuringDay()+AcquirerDrEntriesDuringDay()-AcquirerCrEntriesDuringDay()-AcquirerEntriesDuringPrvDay()
    issuer = MirrorCrEntriesDuringDay() +IssuerCrEntriesDuringDay()-IssuerDrEntriesDuringDay()-IssuerEntriesDuringPrvDay()
    acqclbal=AcquirerDrEntriesDuringDay()-AcquirerCrEntriesDuringDay()
    issclbal=IssuerCrEntriesDuringDay()-IssuerDrEntriesDuringDay()
    recondate = ReconDate.objects.all()[0]
    accountType = AccountType.objects.filter(type='Mirror Account')
    account = Account.objects.filter(accountType=accountType[0])
    axisBankBalMirror=clbalance(account[0].number,recondate.date)
    acqwdlntsl=AcqDuringdayNTSL(recondate.date)
    issddntsl=IssuerDuringdayNTSL(recondate.date)
    issddrgcs=IssuerDuringdayRGCS(recondate.date)
    if issddntsl==None:
        issddntsl=0
    if issddrgcs==None:
        issddrgcs=0
    issddtotal=issddntsl+issddrgcs
    if acqwdlntsl==None:
        acqwdlntsl=0
    acqdiff=acq-acqwdlntsl
    issuerdiff=issuer-issddntsl-issddrgcs
    acqfee=AcquirerFeeTotal(recondate.date)
    acqfeegst=AcquirerFeeGSTTotal(recondate.date)
    issfee = IssuerFeeTotal(recondate.date)
    issfeegst = IssuerFeeGSTTotal(recondate.date)
    issnpciswfee=IssuerNPCIFeeTotal(recondate.date)
    issnpciswfeegst = IssuerNPCIFeeGSTTotal(recondate.date)

    othFeeAmtDr=othFeeTotalRGCS(recondate.date)
    othFeeGSTAmtDr = othFeeGSTTotalRGCS(recondate.date)

    accountType = AccountType.objects.filter(type='Axis Bank')
    accountobj = Account.objects.filter(accountType=accountType[0])
    print(accountobj)
    axisBankBal=clbalance(accountobj[0].number,recondate.date)
    tipduringday = TipDuringdayRGCS(recondate.date)
    adjustedAxisBankBal = axisBankBalMirror + acqfee + acqfeegst - issfee - issfeegst - issnpciswfee - issnpciswfeegst + acqclbal - issclbal-othFeeAmtDr-othFeeGSTAmtDr+tipduringday
    diffAxisBank=adjustedAxisBankBal-axisBankBal
    pendingEntriesTotal=PendingEntriesTotal(recondate.date)
    context={'acq':acq,'issuer':issuer, 'date':recondate.date,'axisbalmirror':axisBankBalMirror,"acqwdlntsl":acqwdlntsl,"acqdiff":acqdiff,"issddntsl":issddntsl,"issuerdiff":issuerdiff,"issddrgcs":issddrgcs,"issddtotal":issddtotal,"acqfee":acqfee,"acqfeegst":acqfeegst,"issfee":issfee,"issfeegst":issfeegst,"issnpciswfee":issnpciswfee,"issnpciswfeegst":issnpciswfeegst,"adjustedAxisBankBal":adjustedAxisBankBal,"acqclbal":acqclbal,"issclbal":issclbal,"othFeeAmtDr":othFeeAmtDr,"othFeeGSTAmtDr":othFeeGSTAmtDr,"axisBankBal":axisBankBal,"diffAxisBank":diffAxisBank,"tipduringday":tipduringday,"pendingEntriesTotal":pendingEntriesTotal}

    return render(request,'recon/recon_dashboard.html',context)

def AcqDuringdayNTSL(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Acquirer WDL Transaction Amount") |
        Q(description="Acquirer WDL Transaction Amount (Micro-ATM)")
    )

    wdl=NTSL.objects.filter(
        Q(description__in=discrptionNTSL) &
        Q(date=cldate)
    ).aggregate(Sum("credit"))

    return wdl["credit__sum"]




def IssuerDuringdayNTSL(cldate):
    discrptionNTSL=Description_NTSL.objects.filter(
        Q(description="Issuer WDL Transaction Amount") |
        Q(description="Issuer WDL Transaction Amount (Micro-ATM)")
    )

    wdl=NTSL.objects.filter(
        (
            Q(description__in=discrptionNTSL)

         ) &
        Q(date=cldate)
    ).aggregate(Sum("debit"))

    return wdl["debit__sum"]

def IssuerDuringdayRGCS(cldate):
    statusRGCS=Status.objects.filter(
        Q(status="A")
    )
    inwardOutwardObj=InwardOutward.objects.filter(
        Q(name="INWARD")
    )

    wdl=RGCS.objects.filter(

        Q(status=statusRGCS[0])&
        Q(inwardOutward=inwardOutwardObj[0])&
        Q(date=cldate)&
        (Q(cycle=4)|Q(cycle=3)|Q(cycle=2))
    ).aggregate(Sum("setAmtDr"))
    wdl1 = RGCS.objects.filter(

        Q(status=statusRGCS[0]) &
        Q(inwardOutward=inwardOutwardObj[0]) &
        Q(date=cldate+timedelta(hours=24)) &
        (Q(cycle=1))
    ).aggregate(Sum("setAmtDr"))
    if wdl["setAmtDr__sum"]==None:
        wdl["setAmtDr__sum"]=0
    if wdl1["setAmtDr__sum"]==None:
        wdl1["setAmtDr__sum"]=0
    return wdl["setAmtDr__sum"]+wdl1["setAmtDr__sum"]

def TipDuringdayRGCS(cldate):


    wdl=TipandSurcharge.objects.filter(

        (Q(status="Pending"))&
        Q(date=cldate)&
        (Q(cycle="POS04")|Q(cycle="POS03")|Q(cycle="POS02"))
    ).aggregate(Sum("finalAmount"))
    wdl1 = TipandSurcharge.objects.filter(

        (Q(status="Pending")) &
        Q(date=cldate+timedelta(hours=24)) &
        (Q(cycle="POS01"))
    ).aggregate(Sum("finalAmount"))
    print(wdl)
    if wdl["finalAmount__sum"]==None:
        wdl["finalAmount__sum"]=0
    if wdl1["finalAmount__sum"]==None:
        wdl1["finalAmount__sum"]=0
    return wdl["finalAmount__sum"]+wdl1["finalAmount__sum"]

def othFeeTotalRGCS(cldate):
    statusRGCS=Status.objects.filter(
        Q(status="A")
    )
    inwardOutwardObj=InwardOutward.objects.filter(
        Q(name="INWARD")
    )

    wdl=RGCS.objects.filter(

        Q(status=statusRGCS[0])&
        Q(inwardOutward=inwardOutwardObj[0])&
        Q(date__lte=cldate)&
        (Q(cycle=4)|Q(cycle=3)|Q(cycle=2))
    ).aggregate(Sum("othFeeAmtDr"))
    wdl1 = RGCS.objects.filter(

        Q(status=statusRGCS[0]) &
        Q(inwardOutward=inwardOutwardObj[0]) &
        Q(date__lte=cldate+timedelta(hours=24)) &
        (Q(cycle=1))
    ).aggregate(Sum("othFeeAmtDr"))
    if wdl["othFeeAmtDr__sum"]==None:
        wdl["othFeeAmtDr__sum"]=0
    if wdl1["othFeeAmtDr__sum"]==None:
        wdl1["othFeeAmtDr__sum"]=0
    return wdl["othFeeAmtDr__sum"]+wdl1["othFeeAmtDr__sum"]

def othFeeGSTTotalRGCS(cldate):

    inwardOutwardObj=InwardOutward.objects.filter(
        Q(name="INWARD GST")
    )

    wdl=RGCS.objects.filter(


        Q(inwardOutward=inwardOutwardObj[0])&
        Q(date__lte=cldate)&
        (Q(cycle=4)|Q(cycle=3)|Q(cycle=2))
    ).aggregate(Sum("othFeeGstDr"))
    wdl1 = RGCS.objects.filter(


        Q(inwardOutward=inwardOutwardObj[0]) &
        Q(date__lte=cldate+timedelta(hours=24)) &
        (Q(cycle=1))
    ).aggregate(Sum("othFeeGstDr"))
    return wdl["othFeeGstDr__sum"]+wdl1["othFeeGstDr__sum"]
def AcquirerFeeTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Acquirer BI Approved Fee")|
        Q(description="Acquirer MS Approved Fee")|
        Q(description="Acquirer WDL Approved Fee")|
        Q(description="Acquirer PC Approved Fee")|
        Q(description="Acquirer WDL Approved Fee  (Micro-ATM)")
    )
    wdl = NTSL.objects.filter(
        Q(description__in=discrptionNTSL) &
        Q(date__lte=cldate)
    ).aggregate(Sum("credit"))

    return wdl["credit__sum"]

def AcquirerFeeGSTTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Acquirer BI Approved Fee - GST")|
        Q(description="Acquirer MS Approved Fee - GST")|
        Q(description="Acquirer WDL Approved Fee - GST")|
        Q(description="Acquirer PC Approved Fee - GST")

    )
    wdl = NTSL.objects.filter(
        Q(description__in=discrptionNTSL) &
        Q(date__lte=cldate)
    ).aggregate(Sum("credit"))

    return wdl["credit__sum"]

def IssuerFeeTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Issuer BI Approved Fee")|
        Q(description="Issuer MS Approved Fee")|
        Q(description="Issuer WDL Approved Fee")|
        Q(description="Issuer PC Approved Fee")|
        Q(description="Issuer WDL Approved Fee (Micro-ATM)")
    )
    wdl = NTSL.objects.filter(
        Q(description__in=discrptionNTSL) &
        Q(date__lte=cldate)
    ).aggregate(Sum("debit"))

def IssuerFeeTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Issuer BI Approved Fee") |
        Q(description="Issuer MS Approved Fee") |
        Q(description="Issuer WDL Approved Fee") |
        Q(description="Issuer PC Approved Fee") |
        Q(description="Issuer WDL Approved Fee (Micro-ATM)")
    )
    wdl = NTSL.objects.filter(
            Q(description__in=discrptionNTSL) &
            Q(date__lte=cldate)
    ).aggregate(Sum("debit"))
    return wdl["debit__sum"]

def IssuerNPCIFeeTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Issuer BI Approved NPCI Switching Fee") |
        Q(description="Issuer MS Approved NPCI Switching Fee") |
        Q(description="Issuer WDL Approved NPCI Switching Fee") |
        Q(description="Issuer PC Approved NPCI Switching Fee") |
        Q(description="Issuer WDL Approved NPCI Switching Fee (Micro-ATM)")
    )
    wdl = NTSL.objects.filter(
            Q(description__in=discrptionNTSL) &
            Q(date__lte=cldate)
    ).aggregate(Sum("debit"))
    return wdl["debit__sum"]

def IssuerNPCIFeeGSTTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Issuer BI Approved NPCI Switching Fee - GST") |
        Q(description="Issuer MS Approved NPCI Switching Fee - GST") |
        Q(description="Issuer WDL Approved NPCI Switching Fee - GST") |
        Q(description="Issuer PC Approved NPCI Switching Fee - GST") |
        Q(description="Issuer WDL Approved NPCI Switching Fee - GST (Micro-ATM)")
    )
    wdl = NTSL.objects.filter(
            Q(description__in=discrptionNTSL) &
            Q(date__lte=cldate)
    ).aggregate(Sum("debit"))
    return wdl["debit__sum"]

def IssuerFeeGSTTotal(cldate):
    discrptionNTSL = Description_NTSL.objects.filter(
        Q(description="Issuer BI Approved Fee - GST")|
        Q(description="Issuer MS Approved Fee - GST")|
        Q(description="Issuer WDL Approved Fee - GST")|
        Q(description="Issuer PC Approved Fee - GST")|
        Q(description="Issuer WDL Approved Fee - GST (Micro-ATM)")
        )
    wdl = NTSL.objects.filter(
            Q(description__in=discrptionNTSL) &
            Q(date__lte=cldate)
        ).aggregate(Sum("debit"))
    return wdl["debit__sum"]


def PendingEntriesTotal(cldate):

    wdl = PendingEntries.objects.filter(
            Q(status="Pending") &
            Q(date__lte=cldate)
        ).aggregate(Sum("debitAmount"))
    wdl1 = PendingEntries.objects.filter(
        Q(status="Pending") &
        Q(date__lte=cldate)
    ).aggregate(Sum("creditAmount"))

    if wdl["debitAmount__sum"]==None:
        wdl["debitAmount__sum"]=0
    if wdl1["creditAmount__sum"]==None:
        wdl1["creditAmount__sum"]=0
    return wdl1["creditAmount__sum"]-wdl["debitAmount__sum"]

def clbalance(accno,cldate):
    account=Account.objects.filter(number=accno)
    ob=(account[0].openingBalance)

    drtxn=Transaction.objects.filter(
        Q(account__number=accno) &
        Q(date__lte=cldate)
    ).aggregate(Sum('drTxn'))

    crtxn = Transaction.objects.filter(
        Q(account__number=accno) &
        Q(date__lte=cldate)
    ).aggregate(Sum('crTxn'))
    if drtxn['drTxn__sum'] == None:
        drtxn['drTxn__sum']=0
    if crtxn['crTxn__sum'] == None:
        crtxn['crTxn__sum']=0

    return ob+float(drtxn['drTxn__sum'])-float(crtxn['crTxn__sum'])

def prdclbalance(accno,cldate):
    account=Account.objects.filter(number=accno)
    ob=(account[0].openingBalance)

    drtxn=Transaction.objects.filter(
        Q(account__number=accno) &
        Q(date__lt=cldate)
    ).aggregate(Sum('drTxn'))

    crtxn = Transaction.objects.filter(
        Q(account__number=accno) &
        Q(date__lt=cldate)
    ).aggregate(Sum('crTxn'))
    return ob+float(drtxn['drTxn__sum'])-float(crtxn['crTxn__sum'])
@login_required
def loadincomingfile(request):
    if request.method == 'POST':
        form = UploadXMLFileForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES['file1'] is not None:
                handleincomingfiles(request.FILES['file1'])
        return redirect('home')
    else:
        form = UploadXMLFileForm()
    return render(request, 'recon/selectincomingfile.html', {'form': form})
@login_required
def loadntslfiles(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            if request.FILES['file1'] is not None:
                handlentslfiles(request.FILES['file1'])
            if request.FILES['file2'] is not None:
                handlentslfiles(request.FILES['file2'])
            if request.FILES['file3'] is not None:
                handlentslfiles(request.FILES['file3'])
            if request.FILES['file4'] is not None:
                handlentslfiles(request.FILES['file4'])

            return redirect('home')

    else:
        form = UploadFileForm()
    return render(request, 'recon/selectntslfile.html', {'form': form})
@login_required
def loadrgcsfiles(request):
    if request.method == 'POST':
        form = UploadRGCSFileForm1(request.POST, request.FILES)
        if form.is_valid():

            if request.FILES['rgcsFile1'] is not None:
                handleRgcsfiles(request.FILES['rgcsFile1'])
            if request.FILES['rgcsFile2'] is not None:
                handleRgcsfiles(request.FILES['rgcsFile2'])
            if request.FILES['rgcsFile3'] is not None:
                handleRgcsfiles(request.FILES['rgcsFile3'])
            if request.FILES['rgcsFile4'] is not None:
                handleRgcsfiles(request.FILES['rgcsFile4'])
            return redirect('home')

    else:
        form = UploadRGCSFileForm1()
    return render(request, 'recon/selectntslfile.html', {'form': form})
def handleincomingfiles(file):
    record = TipandSurcharge()
    doc=xml.dom.minidom.parse(file)
    Hdr=doc.getElementsByTagName("Hdr")[0]
    nDtSet=Hdr.getElementsByTagName("nDtSet")[0]
    date=nDtSet.firstChild.nodeValue
    day = int(date[4:6])
    month = int(date[2:4])
    year = int(date[0:2])+ 2000
    record.date = datetime.datetime(year, month, day)

    nProdCd = Hdr.getElementsByTagName("nProdCd")[0]

    record.cycle=nProdCd.firstChild.nodeValue


    totalAmt=doc.getElementsByTagName("nRnTtlAmt")

    record.finalAmount=float(totalAmt[0].firstChild.nodeValue)/100

    record.status="Pending"


    record.save()

def handlentslfiles(file):


    wb = xlrd.open_workbook(filename=None,file_contents=file.read())
    #wb = file.get_book()
    sheet=wb.sheet_by_index(0)
    row_count = sheet.nrows

    col_count = sheet.ncols
    sheetnames = wb.sheet_names()
    cycle = sheetnames[0][-2:]

    for cur_row in range(0, row_count):
        if cur_row<3:
            pass
        else:
            cell = sheet.cell(cur_row, 0)
            if cell.value=="Dispute Adjustments":
                break
            if cell.value !="":
                record = NTSL()
                description = Description_NTSL.objects.filter(description=cell.value)

                if description == None:
                    print(cell.value + " add NTSL description first")
                    break
                record.description=description[0]

                cell = sheet.cell(cur_row, 1)
                if cell.value=='':
                    record.nooftxns=0
                else:
                    record.nooftxns=cell.value
                cell = sheet.cell(cur_row, 2)
                if cell.value=='':
                    record.debit=0
                else:
                    record.debit = cell.value
                cell = sheet.cell(cur_row, 3)
                if cell.value=='':
                    record.credit=0
                else:
                    record.credit = cell.value
                record.cycle=cycle
                year=int(sheetnames[0][11:13])+2000
                month=int(sheetnames[0][9:11])
                day=int(sheetnames[0][7:9])
                record.date=datetime.datetime(year,month,day)

                recexist=NTSL.objects.filter(
                    Q(date=record.date) &
                    Q(cycle=record.cycle) &
                    Q(description=record.description)
                )
                record.status="Pending"
                if len(recexist)==0:
                    record.save()

              #  print(cell.value, cell.ctype)
        # use sheet.row_len() to get the effective column length when you set ragged_rows = True

def handleRgcsfiles(file):
    wb = xlrd.open_workbook(filename=None, file_contents=file.read())
    # wb = file.get_book()

    sheet = wb.sheet_by_index(0)
    row_count = sheet.nrows

    col_count = sheet.ncols

    cycle = (file.name[-6:])[1:2]

    recdate=None
    productName=None
    bankName=None
    settlementBin=None
    AccId=None
    inwardoutward=None
    status=None
    for cur_row in range(0, row_count):
        if cur_row < 1:
            pass
        else:
            record = RGCS()
            record.cycle=cycle
            cell = sheet.cell(cur_row, 0)

            if cell.value.strip() != "" and cell.value!="NOTE:":
                    day = int(cell.value[0:2])
                    print("day"+str(day))
                    month = int(cell.value[3:5])
                    print("month" + str(month))
                    year = int(cell.value[6:10])
                    print("year"+str(year))
                    recdate=datetime.datetime(year, month, day)

            record.date = recdate



            cell = sheet.cell(cur_row, 1)
            if cell.value != "":
                productName=cell.value
            record.productName = productName

            cell = sheet.cell(cur_row, 2)
            if cell.value != "":
                bankName=cell.value
            record.bankName = bankName

            cell = sheet.cell(cur_row, 3)
            if cell.value.strip() != "":
                settlementBin=cell.value.strip()
            record.settlementBin = settlementBin

            cell = sheet.cell(cur_row, 4)
            if cell.value != "" and cell.value != "Total":
                AccId=cell.value
            record.acqId = AccId

            cell = sheet.cell(cur_row, 5)


            if cell.value != "":
                inwardOutward = cell.value
            if inwardOutward!="Total":
                inwardOutwardobj = InwardOutward.objects.filter(name=inwardOutward)
                record.inwardOutward = inwardOutwardobj[0]

            cell = sheet.cell(cur_row, 6)

            if cell.value.strip() != "":
                status=cell.value.strip()
            if inwardOutward == "Total":
                status=None

            if status!=None:
                statusobj = Status.objects.filter(status=status)
                record.status = statusobj[0]

            cell = sheet.cell(cur_row, 7)

            if cell.value != "":
                transactionCycle = TransactionCycle.objects.filter(transactionCycle=cell.value)
                record.transactionCycle = transactionCycle[0]

            cell = sheet.cell(cur_row, 8)
            if cell.value != "":
                transactionType = TransactionType.objects.filter(transactionType=cell.value)
                record.transactionType = transactionType[0]

            cell = sheet.cell(cur_row, 9)
            channel=cell.value.strip()
            if channel != "":
                channelobj = Channel.objects.filter(channel=cell.value)
                record.channel = channelobj[0]

            cell = sheet.cell(cur_row, 10)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.txnCount = cell.value
                if record.txnCount=="":
                    record.txnCount=None

            cell = sheet.cell(cur_row, 11)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.txnCCY = cell.value
                if record.txnCCY=="":
                    record.txnCCY=None
            cell = sheet.cell(cur_row, 12)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.txnAmtDr = cell.value
                if record.txnAmtDr=="":
                    record.txnAmtDr=None
            cell = sheet.cell(cur_row, 13)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.txnAmtCr = cell.value
                if record.txnAmtCr=="":
                    record.txnAmtCr=None

            cell = sheet.cell(cur_row, 14)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.setCCY = cell.value
                if record.setCCY=="":
                    record.setCCY=None

            cell = sheet.cell(cur_row, 15)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.setAmtDr = cell.value
                if record.setAmtDr=="":
                    record.setAmtDr=None

            cell = sheet.cell(cur_row, 16)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.setAmtCr = cell.value
                if record.setAmtCr=="":
                    record.setAmtCr=None

            cell = sheet.cell(cur_row, 17)
            if (cell.value != "" and channel != "") or inwardOutward == "INWARD GST":
                record.intFeeAmtDr = cell.value
                if record.intFeeAmtDr=="":
                    record.intFeeAmtDr=None
            cell = sheet.cell(cur_row, 18)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.intFeeAmtCr = cell.value
                if record.intFeeAmtCr=="":
                    record.intFeeAmtCr=None

            cell = sheet.cell(cur_row, 19)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.memIncFeeAmtDr = cell.value
                if record.memIncFeeAmtDr=="":
                    record.memIncFeeAmtDr=None

            cell = sheet.cell(cur_row, 20)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.memIncFeeAmtCr = cell.value
                if record.memIncFeeAmtCr=="":
                    record.memIncFeeAmtCr=None

            cell = sheet.cell(cur_row, 21)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.customerCompensationDr = cell.value
                if record.customerCompensationDr=="":
                    record.customerCompensationDr=None

            cell = sheet.cell(cur_row, 22)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.customerCompensationCr = cell.value
                if record.customerCompensationCr=="":
                    record.customerCompensationCr=None

            cell = sheet.cell(cur_row, 23)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.othFeeAmtDr = cell.value
                if record.othFeeAmtDr=="":
                    record.othFeeAmtDr=None
            cell = sheet.cell(cur_row, 24)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.othFeeAmtCr = cell.value
                if record.othFeeAmtCr=="":
                    record.othFeeAmtCr=None

            cell = sheet.cell(cur_row, 25)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.othFeeGstDr = cell.value
                if record.othFeeGstDr=="":
                    record.othFeeGstDr=None
            cell = sheet.cell(cur_row, 26)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.othFeeGstCr = cell.value
                if record.othFeeGstCr=="":
                    record.othFeeGstCr=None

            cell = sheet.cell(cur_row, 27)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.finalSumDr = cell.value
                if record.finalSumDr=="":
                    record.finalSumDr=None
            cell = sheet.cell(cur_row, 28)
            if (cell.value != "" and channel != "") or inwardOutward == "INWARD GST":
                record.finalSumCr = cell.value
                if record.finalSumCr=="":
                    record.finalSumCr=None

            cell = sheet.cell(cur_row, 29)
            if (cell.value != "" and channel != "")or inwardOutward=="INWARD GST":
                record.finalNet = cell.value
                if record.finalNet=="":
                    record.finalNet=None
            record.postingstatus = "Pending"
            if  channel  or inwardOutward == "INWARD GST":
                recexist = RGCS.objects.filter(
                    Q(date=record.date) &
                    Q(cycle=record.cycle) &
                    Q(inwardOutward=record.inwardOutward) &
                    Q(status=record.status) &
                    Q(transactionCycle=record.transactionCycle) &
                    Q(transactionType=record.transactionType) &
                    Q(channel=record.channel)

                )
                if len(recexist) == 0:
                    record.save()



