from django.forms import ModelForm
from .models import AccountType,Account,Transaction,TxnType

class AccountTypeForm(ModelForm):
    class Meta:
        model=AccountType
        fields='__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'
class TxnTypeForm(ModelForm):
    class Meta:
        model = TxnType
        fields = '__all__'