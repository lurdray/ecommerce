from django.shortcuts import render
from customer.models import Customer, WishList, WishListProductConnector

# Create your views here.
def AddCustomerView(request):
	context = {}
	return render(request, 'customer/add_customer.html', context)
	
def AllCustomersView(request):
	customers = Customer.objects.order_by("-pub_date")
	context = {"customers": customers}
	return render(request, 'customer/all_customers.html', context)
	
def CustomerDetailView(request):
	context = {}
	return render(request, 'customer/customer_detail.html', context)
	
def EditCustomerView(request):
	context = {}
	return render(request, 'customer/edit_customer.html', context)
	
def DeleteCustomerView(request):
	pass
	

################wishlist and stuff

def AddToWishList(request, product_id):
	#customer =
	
	wishlist = WishList.objects.create(customer=customer)
	wishlist.save()
	wp = WishListProductConnector(wishlist=wishlist, product=product)
	wp.save()
	pass
	
def LoginView(request):
	context = {}
	return render(request, 'customer/login.html', context)
	
	
