
from django.shortcuts import render
from .models import Account
# Create your views here.
def home(request):
    accounts=Account.objects.all()
    context={'accounts':accounts}
    return render(request,'home.html',context)