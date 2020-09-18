from django.shortcuts import render
from product.models import Product, Review
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
	reviews = Review.objects.order_by("-pub_date")[:10]
	context = {"products": products, "customers": customers, "orders": orders, "reviews": reviews}
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
	
	
	
def DashboardAllReviewsView(request):
	reviews = Review.objects.order_by("-pub_date")
	context = {"reviews": reviews}
	return render(request, 'admin_app/all_review.html', context)
	
	
def DashboardLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))
	



##########polls shit
def AddPollView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'admin_app/all_poll.html', context)
		

	else:
		context ={}
		return render(request, 'admin_app/add_poll.html', context)
		

	


def EditPollView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'admin_app/edit_poll.html', context)
		

	else:
		context ={}
		return render(request, 'admin_app/edit_poll.html', context)



def DeletePollView(request):
	if request.method == "POST":
		pass
		

	else:
		pass



def AllPollView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'admin_app/all_poll.html', context)
		

	else:
		context ={}
		return render(request, 'admin_app/all_poll.html', context)
		





def PollDetailView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'admin_app/poll_detail.html', context)
		

	else:
		context ={}
		return render(request, 'admin_app/poll_detail.html', context)



		

def PollResultView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'admin_app/poll_result.html', context)
		

	else:
		context ={}
		return render(request, 'admin_app/poll_result.html', context)

	

	

