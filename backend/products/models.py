from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=255)

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='products',null=True)