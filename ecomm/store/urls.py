from django.urls import path
from .views import *

urlpatterns = [
        #Leave as empty string for base url
	path('',store,name="store"),
	path('cart/',cart,name="cart"),
	path('checkout/',checkout,name="checkout")
]