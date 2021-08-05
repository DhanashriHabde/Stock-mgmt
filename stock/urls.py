from django.urls import path,include
from . import stockview as sviews
from . import itemview as iviews


urlpatterns = [
    path('',iviews.add_item,name='add_item'),
    path('edititem/<int:id>',iviews.edit_item,name='edit_item'),
    path('deleteitem/<int:id>',iviews.delete_item,name='delete_item'),



    path('add_stock',sviews.add_stock,name='add_stock'),
    path('view',sviews.stock_list,name='view_stock'),
    path('edit/<int:id>',sviews.edit_stock,name='edit_stock'),
    path('delete/<int:id>',sviews.delete_stock,name='delete_stock'),
]