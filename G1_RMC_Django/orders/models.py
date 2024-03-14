from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models import Sum
from invoices.models import Invoice

# Create your models here.
class order(models.Model):
    oid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=200)
    contactno = PhoneNumberField()
    grade = models.CharField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    totalbatch = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True) 


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Call the "real" save() method.
        
        # Get or create the Invoice object for this clientname and grade
        invoice, created = Invoice.objects.get_or_create(
            client=self.clientname, 
            grade=self.grade,
            defaults={'total_quantity': 0, 'total_value': 0}
        )
        
        # Update the total_quantity and total_value of the Invoice
        orders = order.objects.filter(clientname=self.clientname, grade=self.grade)
        invoice.total_quantity = orders.aggregate(Sum('quantity'))['quantity__sum']
        invoice.total_value = orders.aggregate(Sum('price'))['price__sum']
        invoice.save()