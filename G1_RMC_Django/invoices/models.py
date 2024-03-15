from django.db import models

class Invoice(models.Model):
    client = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    total_quantity = models.IntegerField()
    gross_value = models.IntegerField()

class Payment(models.Model):
    payment_date = models.DateField(auto_now_add=True)
    payment_amt = models.IntegerField()
    invoice = models.ForeignKey(Invoice, related_name='payments', on_delete=models.CASCADE)
