from django import forms
from .models import Wallet


class BalanceUpdateForm(forms.ModelForm):
    balance = forms.IntegerField()

    class Meta:
        model= Wallet
        fields = ['balance']
