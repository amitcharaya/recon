
from django.shortcuts import render,redirect
from .models import Account,Transaction,AccountType,TxnType
from .forms import AccountTypeForm,AccountForm,TransactionForm,TxnTypeForm

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