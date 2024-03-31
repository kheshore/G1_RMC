from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    unit_price = models.CharField(max_length=200)

class Invoice(models.Model):
    date = models.DateField()
    client_name = models.CharField(max_length=200)
    billing = models.CharField(max_length=200)
    delivery = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=200)
    items = models.ManyToManyField(Item)
    total = models.CharField(max_length=200)

class OCRResult(models.Model):
    image = models.ImageField(upload_to='ocr_images/')
    extracted_text = models.TextField()
    data = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True, blank=True)
