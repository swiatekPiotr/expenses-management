import datetime

from django import forms
from .models import Expense, Category


class ExpenseSearchForm(forms.ModelForm):
    date_from = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    category_tuple = ((obj.id, obj.name) for obj in Category.objects.all())
    categories = forms.MultipleChoiceField(choices=category_tuple)

    algorithm_choices = [
        ('1', 'sorting by date descending'),
        ('2', 'sorting by date ascending'),
        ('3', 'sorting by category descending'),
        ('4', 'sorting by category ascending')
    ]
    algorithm = forms.CharField(label='Select algorithm', widget=forms.Select(choices=algorithm_choices))

    class Meta:
        model = Expense
        fields = ('name', 'date_from', 'date_to', 'categories')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['date_from'].required = False
        self.fields['date_to'].required = False
        self.fields['categories'].required = False
        self.fields['algorithm'].required = False
