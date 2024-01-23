from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup")
]