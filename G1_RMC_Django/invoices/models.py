from django.db import models

class Invoice(models.Model):
    client = models.CharField(max_length=200)
    grade = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    total_quantity = models.IntegerField()
    total_value = models.IntegerField()

