from django.shortcuts import render
from django.shortcuts import redirect
from .models import Product, Order
from django.db.models import Sum
from .models import Order
from django.db.models import Q
from .models import Product
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.db.models import Count

# Create your views here.
# 在 mysite/views.py 文件中定义视图函数
from django.http import HttpResponse

def index(request):
    return render(request, 'Shopping_app/index.html')

from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})


def add_to_cart_view(request):
    product_id = request.POST.get('product_id')
    product = Product.objects.get(id=product_id)
    order = Order.objects.create(
        product=product,
        quantity=1,
        total_price=product.price,
        customer_name='John Doe',
        customer_email='johndoe@example.com'
    )
    return redirect('product_list')

def order_list_view(request):
    orders = Order.objects.all()
    total_sales = Order.objects.aggregate(Sum('total_price'))
    return render(request, 'order_list.html', {'orders': orders, 'total_sales': total

def product_search_view(request):
    query = request.GET.get('q')
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )
    return render(request, 'product_search.html', {'products': products})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')

def order_chart_view(request):
    chart_data = Order.objects.values('product__name').annotate(count=Count('product')).order_by('-count')[:10]
    chart_labels = [item['product__name'] for item in chart_data]
    chart_values = [item['count'] for item in chart_data]
    chart_data = {'labels': chart_labels, 'values': chart_values}
    return JsonResponse(json.dumps(chart_data), safe=False)
