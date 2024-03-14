from django.shortcuts import get_object_or_404, render ,redirect 
from .models import order
from .forms import OrderForm
from django.urls import reverse
from invoices.models import Invoice

# Create your views here.

def orders(request):
    orders = order.objects.all()
    return render(request,'orders/orders.html' ,{'orders' : orders})

def updateOrder(request, oid):
    order_instance = get_object_or_404(order, oid=oid)  # Make sure 'order' is the correct model class name
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order_instance)  # Use order_instance here
        if form.is_valid():
            form.save()
            return redirect('orders')  # replace with the name of your orders page
    else:
        form = OrderForm(instance=order_instance)  # And also here
    return render(request, 'orders/update_order.html', {'form': form})

def deleteOrder(request, oid):
    order_instance = get_object_or_404(order, oid=oid)
    if request.method == 'POST':
        order_instance.delete()
        return redirect('orders')  # replace with the name of your orders page view function
    return redirect('orders')  

def createOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})
