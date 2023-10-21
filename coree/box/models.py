from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    file = models.FileField(upload_to='files/', null=True, blank=True)
    
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    
    def __str__(self):
        return self.name