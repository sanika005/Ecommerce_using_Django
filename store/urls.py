from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('',views.allProducts, name='all_products'),
    path('item/<slug:slug>', views.product_details, name='product_detail'),
    path('search/<slug:category_slug>', views.category_list, name='category_list')
]
