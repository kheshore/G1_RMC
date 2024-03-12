from django.db import models

# Create your models here.
class client(models.Model):
    cid = models.AutoField(primary_key=True)
    clientname = models.CharField(max_length=200)
    quantity = models.IntegerField()    
    value = models.IntegerField()
    pending = models.IntegerField()