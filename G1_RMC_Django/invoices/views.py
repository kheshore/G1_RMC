from .forms import PaymentForm
from django.db.models import Sum
from .models import Invoice, Payment
from django.shortcuts import render, redirect

# Create your views here.

def Invoices(request):
    invoices = Invoice.objects.all()  # Fetch all Invoice objects
    for invoice in invoices:
        total_payment = Payment.objects.filter(invoice=invoice).aggregate(Sum('payment_amt'))['payment_amt__sum'] or 0
        invoice.total_payment = total_payment
    return render(request, 'invoices/invoices.html', {'invoices': invoices})


def add_Invoice(request):
    return render(request,'invoices/add_Invoice.html')


def add_Payment(request, invoice_id):  # Change 'id' to 'invoice_id'
    invoice = Invoice.objects.get(id=invoice_id)  # Use 'invoice_id' here
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            Payment.objects.create(payment_amt=form.cleaned_data['payment_amt'], invoice=invoice)
            return redirect('invoices')  # Redirect back to the invoice list
    else:
        form = PaymentForm()
    return render(request, 'invoices/add_payment.html', {'form': form})
