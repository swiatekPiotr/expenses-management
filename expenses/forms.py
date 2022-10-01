import datetime

from django import forms
from .models import Expense


class ExpenseSearchForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Expense
        fields = ('name', 'date_from', 'date_to')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date_from'].required = False
        self.fields['date_to'].required = False
