from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('add', views.add_book, name="add_book"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("remove_cart/<int:id>", views.remove_cart, name="remove_cart"),
    path("cart", views.cart, name="cart"),
    path("update_cart/<int:id>", views.update_cart, name="update_cart"),
]


    
    
    