from django.db import models
from stock.itemmodel import Item

# Create your models here.
# Create your models here.
class DistributeStock(models.Model):
    stock_name=models.ForeignKey(Item,on_delete=models.CASCADE)
    section=models.CharField(max_length=20)
    no_of_students=models.DecimalField(max_digits=10, decimal_places=2)
    quantity_per_student=models.DecimalField(max_digits=10, decimal_places=2)
    date=models.CharField(max_length=20)
    
    tquantity=models.DecimalField(max_digits=20, decimal_places=2)
    submitted_at=models.DateField(auto_now_add=True,null=True)
    updated_at=models.DateField(auto_now=True,null=True)

    