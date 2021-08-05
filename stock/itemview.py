from django.shortcuts import render,redirect
from stock.itemmodel import Item
from stock.itemform import ItemForm
from django.contrib import messages

def add_item(request):
    item_data=Item.objects.all()
    if request.method == 'POST':
        item_form=ItemForm(request.POST)
        if item_form.is_valid():
            try:
                if Item.objects.filter(name__iexact=item_form.cleaned_data['name']).exists():
                    messages.error(request,'Item Already Exist')
                    return redirect('add_item')
                else:
                    item_model=Item()
                    item_model.name=item_form.cleaned_data['name']
                    item_model.total=0
                    item_model.save()
                    messages.success(request,'Item added successfully')

        

                    return redirect('add_item')
            except:
                messages.error(request,'Something went wrong')
                return redirect('add_item')
        else:
            messages.error(request,'Entry is invalid')

    else:
        item_form=ItemForm()
    context={
        'page_title':'Item/',
        'page_path' : 'Add Item',
        'menu_icon' : "nav nav-icon fa fa-shopping-basket ",
        'item_form' : item_form,
        'item_data' : item_data,
        }
    return render(request,'webpages/item.html',context)



def edit_item(request,id):
    item_data=Item.objects.all()
    if request.method=='POST':
        i=Item.objects.get(pk=id)
        item_form=ItemForm(request.POST,instance=i)
        if item_form.is_valid():
            try:
                item=item_form.save()
                messages.success(request,'Item Edited Successfully')
                return redirect('add_item')
            except:
                messages.error(request,'Invalid Entry')
                return redirect('add_item')
        else:
            messages.error(request,'Form is invalid')
    else:
        i=Item.objects.get(pk=id)
        item_form=ItemForm(instance=i)
    context={
        'page_title' :'Item /',
        'page_path' :'Edit Item',
        'menu_icon':"nav-icon fa fa-shopping-basket",
        'item_form' : item_form,
        'item_data' : item_data,
    }
    return render(request,'webpages/item.html',context)



def delete_item(request,id):
    if request.method =='POST':
        i=Item.objects.get(pk=id)
        i.delete()
        messages.success(request,'Item deleted successfully')
        return redirect('add_item')