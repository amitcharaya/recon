from django.forms import ModelForm
from .models import AccountType

class AccountTypeForm(ModelForm):
    class Meta:
        model=AccountType
        fields='__all__'