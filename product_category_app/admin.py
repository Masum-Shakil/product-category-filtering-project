from django.contrib import admin
from .models import product_models

# Register your models here.
admin.site.register(product_models.Brands)
admin.site.register(product_models.Sellers)
admin.site.register(product_models.Warranties)
admin.site.register(product_models.ProductTypes)
admin.site.register(product_models.Products)
