from django import forms
from stock.itemmodel import Item

class ItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter Item Name'}),label = 'Item Name',max_length =50,required=True)
    class Meta:
        model = Item
        fields = ('name',)