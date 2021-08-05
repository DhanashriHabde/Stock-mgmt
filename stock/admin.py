from django.contrib import admin
from stock.stockmodel import Stock
from stock.itemmodel import Item
# Register your models here.
admin.site.register(Stock)
admin.site.register(Item)