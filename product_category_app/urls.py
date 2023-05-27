from django.urls import path,include
from .views import product_views

product_patterns = [
    path('', product_views.product_filtering_index_view),
    path('ajax-load/', product_views.realtine_ajax_view, name = 'ajax-load')
]

urlpatterns = [
    path('', include(product_patterns)),   
]
