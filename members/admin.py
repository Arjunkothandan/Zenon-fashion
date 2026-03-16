from django.contrib import admin
from .models import Catagory, Cart
from .models import Product, Order

admin.site.register(Catagory)
admin.site.register(Cart)
admin.site.register(Product)
admin.site.register(Order)

# Register your models here.
