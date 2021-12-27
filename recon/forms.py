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


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction

        fields = '__all__'
        widgets = {
            'date': DateInput(),
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

class UploadFileForm(forms.Form):
    file1 = forms.FileField()
    file2 = forms.FileField()
    file3 = forms.FileField()
    file4 = forms.FileField()



class UploadRGCSFileForm1(forms.Form):
    rgcsFile1 = forms.FileField()
    rgcsFile2 = forms.FileField()
    rgcsFile3 = forms.FileField()
    rgcsFile4 = forms.FileField()

class UploadXMLFileForm(forms.Form):
    file1 = forms.FileField()