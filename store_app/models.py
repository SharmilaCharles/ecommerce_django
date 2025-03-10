from ssl import create_default_context
from unicodedata import category
from django.db import models
from category_app.models import Category
from django.urls import reverse

class Product(models.Model):
    product_name = models.CharField(max_length=50, unique= True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modifies_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse ('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
    
