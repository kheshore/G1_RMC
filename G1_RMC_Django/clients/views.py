from django.shortcuts import render
from .models import client

# Create your views here.
def clientsView(request):
    clients = client.objects.all()  # Query all clients
    return render(request, 'clients/clients.html', {'clients': clients})
