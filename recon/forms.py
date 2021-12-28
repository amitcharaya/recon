from django.forms import ModelForm
from .models import AccountType,Account,Transaction,TxnType,ReconDate,PendingEntries
from django import forms
class DateInput(forms.DateInput):
    input_type = 'date'

class AccountTypeForm(ModelForm):
    class Meta:
        model=AccountType
        fields='__all__'

class AccountForm(ModelForm):

    class Meta:
        model = Account
        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }
        labels = {
            'number':'Account Number',
            'name': 'Account Name',
            'openingBalance':'Opening Balance',
            'date':'Date',
            'accountType':'Account Type'
        }

        error_messages = {
            'name': {
                'max_length': "Account name is too long.",
            },
        }



class TransactionForm(ModelForm):
    class Meta:
        model = Transaction

        fields = '__all__'
        widgets = {
            'date': DateInput(),
        }

        labels = {
            'drTxn': 'Debit Amount',
            'crTxn': 'Credit Amount',
            'txnType': 'Type',

        }
class TxnTypeForm(ModelForm):
    class Meta:
        model = TxnType
        fields = '__all__'

class ReconDateFrom(ModelForm):
    class Meta:
        model = ReconDate
        fields = '__all__'

        widgets = {
            'date': DateInput(),
        }
class PendingEntryForm(ModelForm):
    class Meta:
        model = PendingEntries
        fields = '__all__'

        widgets = {
            'date': DateInput(),
            'adjustmentDate': DateInput(),
        }
        labels = {
            'debitAmount': 'Debit Amount',
            'creditAmount': 'Credit Amount',
            'adjustmentDate': 'Adjustment Date',

        }

class UploadFileForm(forms.Form):
    file1 = forms.FileField(label='Cycle 1')
    file2 = forms.FileField(label='Cycle 2')
    file3 = forms.FileField(label='Cycle 3')
    file4 = forms.FileField(label='Cycle 4')




class UploadRGCSFileForm1(forms.Form):
    file1 = forms.FileField(label='Cycle 2 Same Day')
    file2 = forms.FileField(label='Cycle 3 Same Day')
    file3 = forms.FileField(label='Cycle 4 Same Day')
    file4 = forms.FileField(label='Cycle 1 Next Day')

class UploadXMLFileForm(forms.Form):
    file1 = forms.FileField(label='Incoming File')