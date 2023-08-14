from django.db import models

from django.db import models

class Product(models.Model):
    # class Meta:
    #     ordering = ["id"]
    name = models.CharField(max_length=60)
    price = models.IntegerField()
    description = models.CharField(max_length=127)
    
