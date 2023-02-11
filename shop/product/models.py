from django.db import models


# Create your models here.
class Product(models.Model):
    Categories = models.TextChoices('Categories', 'Clothes Sport Electronics Home Toys')
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=20, choices=Categories.choices)
    description = models.TextField(max_length=200)
