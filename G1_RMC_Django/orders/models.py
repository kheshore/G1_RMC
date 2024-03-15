from django.db import models
from invoices.models import Invoice
from phonenumber_field.modelfields import PhoneNumberField

class order(models.Model):
    oid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=200)
    contactno = PhoneNumberField()
    grade = models.CharField()
    quantity = models.IntegerField()
    rate = models.IntegerField()
    totalbatch = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    invoiceid = models.ForeignKey(Invoice, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # Check if this Order object has been saved to the database
        if self.pk is not None:
            # If it has, update the existing Invoice object
            self.invoiceid.client = self.clientname
            self.invoiceid.grade = self.grade
            self.invoiceid.total_quantity = self.quantity
            self.invoiceid.gross_value = self.rate * self.quantity
            self.invoiceid.save()
        else:
            # If it hasn't, create a new Invoice object
            invoice = Invoice.objects.create(
                client=self.clientname, 
                grade=self.grade,
                total_quantity=self.quantity,
                gross_value= self.rate * self.quantity 
            )
            # Link the invoice to this order
            self.invoiceid = invoice
        super().save(*args, **kwargs)  # Call the "real" save() method.





