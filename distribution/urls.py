from django.urls import path,include
from . import views


urlpatterns = [
    path('distribute_stock/',views.distribute_stock,name='distribute'),
    path('distribute_list/',views.distributed_list,name='distlist'),
    path('reports/',views.report,name='reports'),
   
]