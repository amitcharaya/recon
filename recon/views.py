
from django.shortcuts import render,redirect
from .models import Account,Transaction
from .forms import AccountTypeForm,AccountForm,TransactionForm,TxnTypeForm

# Create your views here.
def home(request):
    transactions = Transaction.objects.all()
    accounts=Account.objects.all()

    context={'accounts':accounts,'transactions':transactions}
    return render(request,'home.html',context)

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