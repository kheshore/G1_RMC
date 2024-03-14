from .models import Invoice  
from django.shortcuts import render

# Create your views here.

def Invoices(request):
    invoices = Invoice.objects.all()  # Fetch all Invoice objects
    return render(request, 'invoices/invoices.html', {'invoices': invoices})


def add_Invoice(request):
    return render(request,'invoices/add_Invoice.html')