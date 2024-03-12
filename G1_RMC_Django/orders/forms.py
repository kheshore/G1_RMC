from django import forms
from .models import order

class OrderForm(forms.ModelForm):
    class Meta:
        model = order
        fields = ['oid','clientname', 'contactno', 'grade', 'quantity', 'price', 'totalbatch']
