from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', product_list_view, name='product_list'),
    path('add_to_cart/', add_to_cart_view, name='add_to_cart'),
    path('orders/', order_list_view, name='order_list'),
    path('products/search/', product_search_view, name='product_search'),
    path('login/', login_view, name='login'),
    path('orders/chart/', order_chart_view, name='order_chart'),
]