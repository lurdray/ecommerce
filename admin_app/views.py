from django.shortcuts import render
from product.models import Product, Review
from order.models import Order
from customer.models import Customer
from poll.models import Poll, PollOptionConnector, Option
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
		title = request.POST.get("title")
		description = request.POST.get("description")
		tag_title = request.POST.get("tag_title")
		category = request.POST.get("category")
		count_down = request.POST.get("count_down")
		poll = Poll.objects.create(title=title, description=description, tag_title=tag_title, category=category, count_down=count_down)

		try:
			if request.FILES["image_1"]:
				image_1 = request.FILES["image_1"]
				poll.image_1 = image_1
			if request.FILES["image_2"]:
				image_2 = request.FILES["image_2"]
				poll.image_2 = image_2
			if request.FILES["image_3"]:
				image_3 = request.FILES["image_3"]
				poll.image_3 = image_3
			else:
				pass

		except:
			pass

		poll.save()


		return HttpResponseRedirect(reverse("dashboard_all_poll"))
		

	else:
		context ={}
		return render(request, 'admin_app/add_poll.html', context)
	




def AddOptionPollView(request, poll_id):
	if request.method == "POST":
		poll = Poll.objects.get(id=poll_id)
		option = request.POST.get("option")
		opt = Option.objects.create(option=option)
		opt.save()
		po = PollOptionConnector(poll=poll, option=opt)
		po.save()

		return HttpResponseRedirect(reverse("dashboard_all_poll"))
		

	else:
		poll = Poll.objects.get(id=poll_id)
		context ={"poll": poll}
		return render(request, 'admin_app/add_option.html', context)	

	


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
		polls = Poll.objects.order_by("-pub_date")
		context ={"polls": polls}

		#return HttpResponse(polls.count())
		return render(request, 'admin_app/all_poll.html', context)
		





def PollDetailView(request, poll_id):
	if request.method == "POST":
		title = request.POST.get("title")
		description = request.POST.get("description")

		poll = Poll.objects.get(id=poll_id)

		poll.title = title
		poll.description = description

		poll.save()
		
		options = poll.options.all()
		context = {"poll": poll, "options": options}
		return render(request, 'admin_app/poll_detail.html', context)
		

	else:
		poll = Poll.objects.get(id=poll_id)
		options = poll.options.all()
		context = {"poll": poll, "options": options}
		return render(request, 'admin_app/poll_detail.html', context)



		

def PollResultView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'admin_app/poll_result.html', context)
		

	else:
		context ={}
		return render(request, 'admin_app/poll_result.html', context)

	

	

