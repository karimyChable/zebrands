from django.contrib import admin

# Register your models here.
from django.urls import path
from .views import *

products_urls = [

    path('products/<uuid:pk>', ProductView.as_view()),
    path('products/', ProductListView.as_view()),

]
