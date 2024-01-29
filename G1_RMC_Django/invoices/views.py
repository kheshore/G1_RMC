from django.shortcuts import render

# Create your views here.

def create_Invoice(request):
    return render(request,'invoices/index.html')