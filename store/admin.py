from django.contrib import admin
from .models.user import User
from .models.category import Category
from .models.product import Product
from .models.order import Order
from .models.address import Address

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "phone_no")

# class CustomProductAdmin(admin.ModelAdmin):
#     list_display = ("name", "category_name")
    

# Register your models here.
admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Address)
