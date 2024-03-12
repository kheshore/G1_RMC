from django.urls import path
from . import views

urlpatterns =[

    path('',views.clientsView, name='clients'),
    
]