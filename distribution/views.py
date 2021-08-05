from django.shortcuts import render,redirect
from django.http import HttpResponse
from stock.stockmodel import Stock 
from stock.itemmodel import Item
from .forms import DistributeForm,StockSearchForm
from .models import DistributeStock
from django.contrib import messages
from django.db.models import Q
from .filters import StockFilter
import xlwt
# Create your views here.


def distribute_stock(request):
    if request.method == 'POST':
        dist_stock_form=DistributeForm(request.POST)
        if dist_stock_form.is_valid():
            try:
                distribute_model=DistributeStock()
                distribute_model.section=dist_stock_form.cleaned_data['section']
                distribute_model.no_of_students=dist_stock_form.cleaned_data['no_of_students']
                distribute_model.quantity_per_student=dist_stock_form.cleaned_data['quantity_per_student']
                distribute_model.stock_name=dist_stock_form.cleaned_data['stock_name']
                distribute_model.date=dist_stock_form.cleaned_data['date']
                
                distribute_model.tquantity=distribute_model.quantity_per_student*distribute_model.no_of_students
                distributed=distribute_model.tquantity
                total=Item.objects.get(name=distribute_model.stock_name)
               
                if distribute_model.tquantity <= total.total :
                    total.total-=distribute_model.tquantity
                    total.save()
                   
                    messages.success(request,'Stock Distributed successfully')
                
                else :
                    messages.error(request,"Stock is not enough ! please add more stock")
                    return redirect('add_stock')
                
                
                distribute_model.save()
                return redirect('distribute')
            except:
                messages.error(request,"Invalid Entry")
                return redirect('distribute')
        else:
            messages.error(request,"Form is not valid !")
            return redirect('distribute')

    else:
        dist_stock_form=DistributeForm()
     
    context={
        'page_title' : "Distribute /",
        'page_path'  : "Distribute Stock",
        'menu_icon' : "fa fas fa-shopping-cart",
        "dist":dist_stock_form, 
       
    }
    return render(request,'webpages/distribute.html',context)


# Stock List View
def distributed_list(request):
    dist=DistributeStock.objects.all()
    context = {
            'page_title':"Stock/",
            "page_path":" Stock List",
            "menu_icon":"nav-icon fas fa-shopping-cart",
            "dist":dist,  
            
            }    
    return render(request, 'webpages/view_distributed.html',context) 

def report(request):
    '''
    form = StockSearchForm(request.POST)
  
    if request.method =='POST':
        if form.is_valid():
            section = form.cleaned_data['section']
            date = form.cleaned_data['date']
            stock_name=form.cleaned_data['stock_name']
        
            #dist=DistributeStock.objects.filter(Q(section=section))
            dist=DistributeStock.objects.filter(Q(stock_name__name=stock_name) |Q(section=section)|Q(date=date))
        
            print(dist)
            context={
            "form":form,
            "dist":dist,
        }
        
    else:
        form =StockSearchForm()
        dist = DistributeStock.objects.all()
        print(dist)
    context={
            "form":form,
            "dist":dist,
        }
    return render(request,'webpages/reports.html',context)
    '''
    dist = DistributeStock.objects.all()
    stock_filter=StockFilter(request.GET,queryset=dist)
    dist=stock_filter.qs

    if request.method == 'POST':
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Shaley_Poshan_Aahar.xls"'
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Distributed stock Data') # this will make a sheet named Users Data
        # Sheet header, first row
        row_num = 0
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
        columns = ['Section','Date','No of students' , 'Stock Name' ,'Quantity per student' , 'Total Quantity(Distributed)']
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
        rows = dist.values_list('section','date','no_of_students','stock_name__name','quantity_per_student','tquantity')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
        wb.save(response)
        return response

    context={
            "stock_filter":stock_filter,
            "dist":dist,
        }
    return render(request,'webpages/reports.html',context)

    
