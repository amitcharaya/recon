import pandas as pd
from datetime import timedelta
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Account,Transaction,AccountType,TxnType,ReconDate,NTSL,NTSL_Dispute_Adjustments,Description_NTSL,InwardOutward,Status,TransactionType,TransactionCycle,Channel,RGCS
from .forms import AccountTypeForm,AccountForm,TransactionForm,TxnTypeForm,ReconDateFrom,UploadFileForm
from django.db.models import Q
from django.db.models import Sum
from django.templatetags.static import static
from django.conf import settings
import os
import xlrd
import datetime
# Create your views here.
def home(request):
    transactions = Transaction.objects.all()
    accounts=Account.objects.all()

    context={'accounts':accounts,'transactions':transactions}
    return render(request,'home.html',context)

def accounts(request):

    accounts=Account.objects.all()

    context={'accounts':accounts}

    return render(request,'recon/accounts.html',context)

def accounttypes(request):

    accounttypes = AccountType.objects.all()

    context = {'accounttypes': accounttypes}
    return render(request, 'recon/account_types.html', context)

def transactions(request):

    transactions = Transaction.objects.all()

    context = {'transactions': transactions}
    return render(request, 'recon/transactions.html', context)


def txntypes(request):

    txntypes = TxnType.objects.all()

    context = {'txntypes': txntypes}
    return render(request, 'recon/transaction_types.html', context)


def createAccountTYpe(request):

    form=AccountTypeForm()
    if request.method=='POST':
        form=AccountTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form':form}
    return render(request, 'recon/account_type_form.html', context)

def createAccount(request):
    form=AccountForm()
    if request.method=='POST':
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'recon/account_form.html',context)

def deleteAccount(request,pk):
    account = Account.objects.get(id=pk)
    if request.method=='POST':
        account.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':account})

def deleteAccounttype(request,pk):
    accounttype = AccountType.objects.get(id=pk)
    if request.method=='POST':
        accounttype.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':accounttype})

def deleteTransaction(request,pk):
    transaction = Transaction.objects.get(id=pk)
    if request.method=='POST':
        transaction.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':transaction})



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

def updateTransaction(request,pk):
    transaction= Transaction.objects.get(id=pk)
    form = TransactionForm(instance=transaction)
    if request.method=='POST':
        form=TransactionForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'recon/transaction_form.html', context)



def createTransaction(request):
    form=TransactionForm()
    if request.method=='POST':
        form=TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'recon/transaction_form.html',context)

def createTxntype(request):
    form=TxnTypeForm()
    if request.method=='POST':
        form=TxnTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'recon/txntype_form.html',context)

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


def deleteTxnType(request,pk):
    txntype = TxnType.objects.get(id=pk)
    if request.method=='POST':
        txntype.delete()
        return redirect('home')
    return render(request,'recon/delete.html',{'obj':txntype})

def createRecondate(request):
    form=ReconDateFrom()
    if request.method=='POST':
        form=ReconDateFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'recon/recondate_form.html',context)

def MirrorCrEntriesDuringDay():
    recondate=ReconDate.objects.get(id=1)
    accountType=AccountType.objects.filter(type='Mirror Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('crTxn'))
    if transactions['crTxn__sum']==None:
        transactions['crTxn__sum']=0
    return transactions['crTxn__sum']

def MirrorDrEntriesDuringDay():
    recondate=ReconDate.objects.get(id=1)
    accountType=AccountType.objects.filter(type='Mirror Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('drTxn'))
    if transactions['drTxn__sum']==None:
        transactions['drTxn__sum']=0
    return transactions['drTxn__sum']

def IssuerDrEntriesDuringDay():
    recondate=ReconDate.objects.get(id=1)
    accountType=AccountType.objects.filter(type='Issuer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('drTxn'))
    if transactions['drTxn__sum']==None:
        transactions['drTxn__sum']=0
    return transactions['drTxn__sum']

def IssuerCrEntriesDuringDay():
    recondate=ReconDate.objects.get(id=1)
    accountType=AccountType.objects.filter(type='Issuer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('crTxn'))
    if transactions['crTxn__sum']==None:
        transactions['crTxn__sum']=0
    return transactions['crTxn__sum']

def AcquirerDrEntriesDuringDay():
    recondate=ReconDate.objects.get(id=1)
    accountType=AccountType.objects.filter(type='Acquirer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions=Transaction.objects.filter(account=account[0],date=recondate.date).aggregate(Sum('drTxn'))
    if transactions['drTxn__sum']==None:
        transactions['drTxn__sum']=0
    return transactions['drTxn__sum']



def AcquirerCrEntriesDuringDay():
    recondate = ReconDate.objects.get(id=1)
    accountType = AccountType.objects.filter(type='Acquirer Account')
    account = Account.objects.filter(accountType=accountType[0])
    transactions = Transaction.objects.filter(account=account[0], date=recondate.date).aggregate(Sum('crTxn'))
    if transactions['crTxn__sum']==None:
        transactions['crTxn__sum']=0
    return transactions['crTxn__sum']

def AcquirerEntriesDuringPrvDay():
    recondate=ReconDate.objects.get(id=1)
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
    recondate=ReconDate.objects.get(id=1)
    accountType=AccountType.objects.filter(type='Issuer Account')
    account = Account.objects.filter(accountType=accountType[0])
    drtransactions=Transaction.objects.filter(account=account[0],date=recondate.date-timedelta(hours=24)).aggregate(Sum('drTxn'))
    crtransactions = Transaction.objects.filter(account=account[0], date=recondate.date - timedelta(hours=24)).aggregate(Sum('crTxn'))

    if drtransactions['drTxn__sum']==None:
        drtransactions['drTxn__sum']=0
    if crtransactions['crTxn__sum']==None:
        crtransactions['crTxn__sum']=0
    return crtransactions['crTxn__sum']-drtransactions['drTxn__sum']

def ReconDashboard(request):
    acq=MirrorDrEntriesDuringDay()+AcquirerDrEntriesDuringDay()-AcquirerCrEntriesDuringDay()-AcquirerEntriesDuringPrvDay()
    issuer = MirrorCrEntriesDuringDay() +IssuerCrEntriesDuringDay()-IssuerDrEntriesDuringDay()-IssuerEntriesDuringPrvDay()
    recondate = ReconDate.objects.get(id=1)
    accountType = AccountType.objects.filter(type='Mirror Account')
    account = Account.objects.filter(accountType=accountType[0])
    clbal=clbalance(account[0].number,recondate.date)
    acqwdlntsl=AcqDuringdayNTSL(recondate.date)
    issddntsl=IssuerDuringdayNTSL(recondate.date)
    issddrgcs=IssuerDuringdayRGCS(recondate.date)
    issddtotal=issddntsl+issddrgcs
    acqdiff=acq-acqwdlntsl
    issuerdiff=issuer-issddntsl-issddrgcs
    context={'acq':acq,'issuer':issuer, 'date':recondate.date,'axisbal':clbal,"acqwdlntsl":acqwdlntsl,"acqdiff":acqdiff,"issddntsl":issddntsl,"issuerdiff":issuerdiff,"issddrgcs":issddrgcs,"issddtotal":issddtotal}

    return render(request,'recon/recon_dashboard.html',context)

def AcqDuringdayNTSL(cldate):
    discrptionNTSL=Description_NTSL.objects.filter(description="Acquirer WDL Transaction Amount")

    wdl=NTSL.objects.filter(
        Q(description=discrptionNTSL[0]) &
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
            Q(description=discrptionNTSL[0])|
            Q(description=discrptionNTSL[1])
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
    return wdl["setAmtDr__sum"]+wdl1["setAmtDr__sum"]

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
        form = UploadFileForm()
    return render(request, 'recon/selectntslfile.html', {'form': form})

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

            if  channel  or inwardOutward == "INWARD GST":
                record.save()



