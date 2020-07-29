from django.shortcuts import render
from product.models import Product
from order.models import Order
from customer.models import Customer
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def DashboardView(request):
	products = Product.objects.order_by("-pub_date")[:10]
	orders = Order.objects.order_by("-pub_date")[:10]
	customers = Customer.objects.order_by("-pub_date")[:10]
	context = {"products": products, "customers": customers, "orders": orders}
	return render(request, 'admin_app/index.html', context)
	

def DashboardProductDetailView(request, slug):
	product = Product.objects.get(slug=slug)
	context = {"product": product}
	return render(request, 'admin_app/product_detail.html', context)

def DashboardOrderDetailView(request, order_id):
	order = Order.objects.get(id=order_id)
	context = {"order": order}
	return render(request, 'order/order_detail.html', context)


def DashboardCustomerDetailView(request):
	context = {}
	return render(request, 'admin_app/customer_detail.html', context)
	
	
	
def DashboardAllProductsView(request):
	products = Product.objects.order_by("-pub_date")
	context = {"products": products}
	return render(request, 'admin_app/all_products.html', context)
	
	
def DashboardLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))
	
	
	

