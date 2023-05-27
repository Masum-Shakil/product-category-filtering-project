from django.db import models

class Brands(models.Model):
    brand_name = models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name

class Sellers(models.Model):
    seller_name = models.CharField(max_length=200)

    def __str__(self):
        return self.seller_name

class Warranties(models.Model):
    warranty_year = models.FloatField()

    def __str__(self):
        return f'{self.warranty_year} years'

class ProductTypes(models.Model):
    types = models.CharField(max_length=200)

    def __str__(self):
        return self.types

class Products(models.Model):
    brand = models.ForeignKey(Brands, on_delete=models.PROTECT, related_name='products_brands')
    seller = models.ForeignKey(Sellers, on_delete=models.PROTECT, related_name='products_sellers')
    warranty = models.ForeignKey(Warranties, on_delete=models.PROTECT, related_name='products_warranty')
    type = models.ForeignKey(ProductTypes, on_delete=models.PROTECT, related_name='products_type')
    product_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    price = models.FloatField()

    def __str__(self):
        return self.product_name