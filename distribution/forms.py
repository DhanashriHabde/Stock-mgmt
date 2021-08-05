from stock.stockmodel import Stock
from django import forms
from .models import DistributeStock
from stock.itemmodel import Item

sections = (
    ('', 'Select Section'),
    ('Primary', 'Primary'),
    ('5th-8th', '5th-8th'),
    ('9th-10th','9th-10th'),
    ('Junior college','Junior college'),
)


class DistributeForm(forms.ModelForm):
    section=forms.ChoiceField(label="Sections",choices=sections,required=True)
    no_of_students=forms.DecimalField(label="No of students",required=True)
    quantity_per_student=forms.DecimalField(label="Quantity per student (gram/ml)",required=True)
    stock_name=forms.ModelChoiceField(widget=forms.Select(attrs={'class':"form-control select2bs4",'style':"width: 100%;",'title': "select Item"}),label="Select Item",queryset=Item.objects.all(),required=True)
    date=forms.CharField(label="Date",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)
    
    

    class Meta:
        model = DistributeStock
        fields = ('section','no_of_students','quantity_per_student','stock_name','date',)

items = Item.objects.all().values_list('name','name')

class StockSearchForm(forms.Form):
        section = forms.ChoiceField(label="Select Section",choices=sections,required=False)
        stock_name = forms.ChoiceField(label="Select Stock",choices=items,required=False)
        date=forms.CharField(label="Select Date",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=False)

