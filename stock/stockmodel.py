from django.db import models
from stock.itemmodel import Item

# Create your models here.
class Stock(models.Model):
    name=models.ForeignKey(Item,on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    quantity=models.DecimalField(max_digits=20, decimal_places=5)
    submitted_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)
