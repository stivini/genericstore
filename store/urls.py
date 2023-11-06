from django.urls import path
from . import views

app_name = "store"

urlpatterns = [
    path(r'products/', views.products, name='prods'),
    path(r'products/<str:name>/', views.spesproducts, name='spess'),
    path(r'remove/<str:name>/', views.remove, name='remove'),
    path(r'login/', views.login , name='login'),
    path(r'signin/', views.sign_in , name='signin'),
    path(r'cart/', views.cart, name='cart'),
    path(r'category/', views.category, name='category'),
    path(r'category/<str:name>/', views.spesscat, name='spesscat'),
    path(r'test/', views.test, name='test'),
    path(r'profile/', views.profile, name='profile'),
    path(r'checkout/', views.checkout, name='checkout'),
    path(r'wishlist/', views.wishlist, name='wishlist'),
    path(r'log/', views.user_login, name='userlogin'),
    path(r'products/<str:username>/<str:name>/purchase/', views.purchase_product, name='product_purchase'),
    ]