from django.urls import path
from . import views
from .views import home_view
from .views import product_list_view
from .views import add_to_cart_view
from .views import order_list_view
from .views import product_search_view
from .views import login_view
from .views import order_chart_view


urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list_view, name='product_list'),
    path('add_to_cart/', add_to_cart_view, name='add_to_cart'),
    path('orders/', order_list_view, name='order_list'),
    path('products/search/', product_search_view, name='product_search'),
    path('login/', login_view, name='login'),
    path('orders/chart/', order_chart_view, name='order_chart'),
]