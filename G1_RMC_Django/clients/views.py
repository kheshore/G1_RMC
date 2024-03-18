from django.db.models import Sum
from django.shortcuts import render
from invoices.models import Invoice

# Create your views here.
def clientsView(request):
    # Query all invoices, group them by client, and sum up the total_value
    allInvoice = Invoice.objects.values('client').annotate(gross_value_sum=Sum('gross_value'))
    return render(request, 'clients/clients.html', {'clients': allInvoice})

