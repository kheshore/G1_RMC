from django.db import models

# Create your models here.
class order(models.Model):
    oid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=200)
    contactno = models.IntegerField()
    grade = models.CharField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    totalbatch = models.IntegerField(default=0)