from django.db import models
from .category import Category

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(default=0, verbose_name="price (₹)")
    image = models.ImageField(upload_to="uploads/products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    @staticmethod
    def get_product(id):
        return Product.objects.get(id=id)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_products_by_category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        return Product.objects.all()
