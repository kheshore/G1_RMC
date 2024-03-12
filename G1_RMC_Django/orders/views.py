from django.shortcuts import get_object_or_404, render ,redirect 
from .models import order
from .forms import OrderForm
from django.http import HttpResponseRedirect  
from django.urls import reverse

# Create your views here.

def orders(request):
    orders = order.objects.all()
    return render(request,'orders/orders.html' ,{'orders' : orders})

def updateOrder(request, oid):
    order = get_object_or_404(order, oid=oid)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('orders/orders.html')  # replace with the name of your orders page
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/update_order.html', {'form': form})

def deleteOrder(request, oid):
    order_instance = get_object_or_404(order, oid=oid)
    order_instance.delete()
    return HttpResponseRedirect(render('orders/orders.html'))  

def createOrder(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    else:
        form = OrderForm()
    return render(request, 'orders/create_order.html', {'form': form})
