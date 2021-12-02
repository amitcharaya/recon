
from django.shortcuts import render
from .models import Account,Transaction
from .forms import AccountTypeForm
# Create your views here.
def home(request):
    transactions = Transaction.objects.all()
    accounts=Account.objects.all()

    context={'accounts':accounts,'transactions':transactions}
    return render(request,'home.html',context)

def createAccountTYpe(request):
    form=AccountTypeForm()
    context={'form':form}
    return render(request, 'recon/account_type_form.html', context)