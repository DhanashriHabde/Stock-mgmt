from django.shortcuts import render,redirect
from stock.stockmodel import Stock 
from stock.itemmodel import Item
from stock.stockform import AddStock
from django.contrib import messages
from django.db.models import Q
from django.db.models import Avg, Count,Sum
# Create your views here.
def home(request):
    return render(request,'layouts/admin_base_layout.html')

def add_stock(request):
    titem=Item.objects.all()
    if request.method == 'POST':
        add_stock_form=AddStock(request.POST)
        if add_stock_form.is_valid():
            try:
                stock_model=Stock()
                stock_model.name=add_stock_form.cleaned_data['name']
                stock_model.date=add_stock_form.cleaned_data['date']
                stock_model.quantity=add_stock_form.cleaned_data['quantity']
                unit=add_stock_form.cleaned_data['unit']
                #converting units
                if unit=='Kg' or unit=='l':
                    stock_model.quantity=stock_model.quantity*1000
                stock_model.save()
                #updating total stock
                total=Item.objects.get(name=stock_model.name)
                total.total=Stock.objects.filter(name__name=stock_model.name).aggregate(sum=Sum('quantity'))['sum']
                total.save()
            
                messages.success(request,'Stock added successfully')

                return redirect('add_stock')
            except:
                messages.error(request,"Invalid Entry")
                return redirect('add_stock')
        else:
            messages.error(request,"Form is not valid !")
            return redirect('add_stock')

    else:
        add_stock_form = AddStock()
     
    context={
        'page_title' : "Stock /",
        'page_path'  : "Add stock",
        'menu_icon' : "fa fas fa-shopping-cart",
        "add_stock_form":add_stock_form,
        'titem':titem, 
    }
    return render(request,'webpages/add_stock.html',context)



# Stock List View
def stock_list(request):
    stock=Stock.objects.all()

    context = {
            'page_title':"Stock/",
            "page_path":" Stock List",
            "menu_icon":"nav-icon fas fa-shopping-cart",
            "stock":stock,  
            
            }    
    return render(request, 'webpages/view_stock.html',context) 



# stock edit Views
def edit_stock(request,id):
    if request.method =='POST':
        stock_edit = Stock.objects.get(pk=id)
        add_stock_form=AddStock(request.POST,instance=stock_edit)

        if add_stock_form.is_valid():
            try:
                add_stock_form.save()
                total=Item.objects.get(name=stock_edit.name)
                total.total=Stock.objects.filter(name__name=stock_edit.name).aggregate(sum=Sum('quantity'))['sum']
                total.save()
                messages.success(request,'Stock Edited successfully !')
                return redirect('view_stock')
            except:
                messages.error(request,"Invalid Entry")
                return redirect('view_stock')
        else:
            messages.error(request,"Form is not valid !")

    else:
        stock_edit = Stock.objects.get(pk=id)
        add_stock_form=AddStock(instance=stock_edit)
    
    context={
        'page_title' : "Stock /",
        'page_path'  : "Add stock",
        'menu_icon' : "fa fas fa-shopping-basket",
        "add_stock_form":add_stock_form,
    }
    return render(request,'webpages/add_stock.html',context)

# Stock Delete View
def delete_stock(request,id):
    if request.method == 'POST':
        sd=Stock.objects.get(pk=id)
        total=Item.objects.get(name=sd.name)
        total.total-=sd.quantity
        sd.delete()
        total.save()
        messages.success(request, 'Stock Deleted Successfully!')
        return redirect('view_stock')