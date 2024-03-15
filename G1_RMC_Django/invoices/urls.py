from django.urls import path
from . import views

urlpatterns =[

    path('',views.Invoices, name='invoices'),
    path('add_Invoice',views.add_Invoice, name='add_Invoice'),
    path('add_Payment/<int:invoice_id>/', views.add_Payment, name='add_Payment'), 
  

]