from django.shortcuts import render 
from ..models import product_models
from django.http import JsonResponse

def product_filtering_index_view(request):
    products = product_models.Products.objects.all()
    brands = product_models.Brands.objects.all()
    product_type = product_models.ProductTypes.objects.all()
    sellers = product_models.Sellers.objects.all()
    warranty = product_models.Warranties.objects.all()

    context = {
        'products': products,
        'brands': brands,
        'product_type': product_type,
        'sellers': sellers,
        'warranty': warranty
    }

    return render(request, 'product_category_app/index.html', context)

def realtine_ajax_view(request):
    category = request.GET.get('category')

    if 'brand:' in category:
        category = category.replace('brand:', '')
        product = product_models.Products.objects.filter(brand__brand_name = category)

    if 'sellers:' in category:
        category = category.replace('sellers:', '')
        product = product_models.Products.objects.filter(seller__seller_name = category)

    if 'warranty:' in category:
        category = category.replace('warranty:', '')
        product = product_models.Products.objects.filter(warranty__warranty_year = category)

    if 'types:' in category:
        category = category.replace('types:', '')
        product = product_models.Products.objects.filter(type__types = category)

    data = {
        'products': list(product.values())
    }
    
    return JsonResponse(data)