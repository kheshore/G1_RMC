from django.urls import path
from . import views

urlpatterns =[

    path('createInvoice/',views.create_Invoice, name='invoices') 

]