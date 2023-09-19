from django.urls import path
from .views import *

app_name = "ecommerce"

urlpatterns = [
    path('',products ,name='products'),
    path('placeOrder/<str:i>/',placeOrder,name='placeOrder'),
    path('addProduct/', addProduct,name='addProduct'),
]