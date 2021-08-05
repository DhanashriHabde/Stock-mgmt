from stock.stockmodel import Stock
from django import forms
from stock.itemmodel import Item

Units = (
    ('', 'Select Unit'),
    ('Kg', 'Kg'),
    ('G', 'g'),
    ('ml', 'Ml'),
    ('l','l'),
    ('None','None'),
)


class AddStock(forms.ModelForm):
    name=forms.ModelChoiceField(widget=forms.Select(attrs={'class':"form-control select2bs4",'style':"width: 100%;",'title': "select Item"}),label="Select Item",queryset=Item.objects.all(),required=True)
    date=forms.CharField(label="Date",widget=forms.TextInput(attrs={'type': 'date','placeholder': 'DD/MM/YYYY'}),empty_value=False,required=True)
    quantity=forms.DecimalField(label="Quantity",required=True)
    unit=forms.ChoiceField(label="Unit",choices=Units,required=True)
    

    class Meta:
        model = Stock
        fields = ('name','date','quantity',)