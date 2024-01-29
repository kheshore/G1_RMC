from django.urls import path
from . import views

urlpatterns =[

    path('',views.Invoices, name='invoices'),
    path('add_Invoice',views.add_Invoice, name='add_Invoice')  

]