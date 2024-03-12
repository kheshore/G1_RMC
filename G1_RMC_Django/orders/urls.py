from django.urls import path
from . import views

urlpatterns =[

    path('',views.orders, name='orders'),
    path('create_order',views.createOrder, name='create_order'),
    path('update_order/<int:oid>/',views.updateOrder, name='update_order'),
    path('delete_order/<int:oid>/',views.deleteOrder, name='delete_order'),
      
]