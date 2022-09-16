from django.contrib import admin
from django.urls import path
from products.views import create_product, list_products, search_products, delete_products,update_products


urlpatterns = [
    path('new-product/', create_product, name='create_product'),
    path('search-products/', search_products, name='search_products'),
    path('all-products/', list_products, name='list_products'),
    path('delete-products/<int:pk>/', delete_products, name='delete_products'),
    path('update-products/<int:pk>/', update_products, name='update_products'),
    ]