import random
import string
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from product.models import Product
from customer.models import Customer
from cart.models import Cart
from order.models import Order
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def ray_randomiser(length=6):
	landd = string.ascii_letters + string.digits
	return ''.join((random.choice(landd) for i in range(length)))
	
def IndexView(request):
	#if request.method == 'GET' and request.GET.get('query') != None:
	if request.method == "POST":
		query = request.POST.get('query')
		category = request.POST.get('category')
		products = Product.objects.filter(name__icontains=query, category=category)
		context = {'products': products}
		return render(request, 'product/all_products.html', context)
		
		
	else:
		if request.user.is_active:
			user = request.user
			user = User.objects.get(id=user.id)
			user_checker = authenticate(username=user.username, password=user.password)
			#pass
			#return HttpResponse("issues ooo!")
		else:
			#return HttpResponse("i reached here ooo!")
			fake_username = "%s" % (ray_randomiser())
			fake_password = "%s" % (ray_randomiser())
			user = User.objects.create(username=fake_username)
			user.save()
			user.set_password(fake_password)
			user.save()
			user_checker = authenticate(username=fake_username, password=fake_password)
			
			if user.is_active:
				login(request, user_checker)
			else:
				pass

			cart = Cart.objects.create(user=user, pub_date=timezone.now())
			cart.user = user
			cart.save()
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
	
		product = Product.objects.all()
		all_products = Product.objects.all()
		section_one = Product.objects.all()[:6]
		section_two = Product.objects.all()[:6]
		section_three = Product.objects.all()[:6]
		section_four = Product.objects.all()[:6]
		section_five = Product.objects.all()[:6]
		
		bedrooms = Product.objects.filter(category="BEDROOM")[:10]
		kitchens = Product.objects.filter(category="KITCHEN & DINNING")[:10]
		living_rooms = Product.objects.filter(category="LIVING ROOM")[:10]
		offices = Product.objects.filter(category="OFFICE")[:10]
		kiddies = Product.objects.filter(category="KIDDIES")[:10]
		acessories = Product.objects.filter(category="ACESSORIES")[:10]
	
		context = {"bedrooms": bedrooms, "kitchens": kitchens, "living_rooms": living_rooms, "offices": offices, "kiddies": kiddies, "acessories": acessories,  "total_price": total_price, "product_quantitys": product_quantitys, "product": product, "all_products": all_products, "section_one": section_one, "section_two": section_two, "section_three": section_three, "section_four": section_four, "section_five": section_five}
		return render(request, 'main/index.html', context)
	
	
def CategoryView(request, category):
	products = Product.objects.filter(category=category)
	all_products = Product.objects.all()
	try:
		product = products[0]
		category = product.category
	except:
		category = "All"
	page_title = "%s Category" % (category)
	
	cart = get_object_or_404(Cart, user__pk=request.user.id)
	product_quantitys = cart.product_quantitys.all()
	total_price = 0
	total_quantity = 0
	for item in product_quantitys:
		total_price += (item.product.price * int(str(item.quantity)))
	
	
	context = {"total_price": total_price, "product_quantitys": product_quantitys, "products": products, "page_title": page_title, "all_products": all_products}
	return render(request, 'product/all_products.html', context)
	
	
def ShopView(request):
	
	if request.method == "POST":
		review = request.POST.getlist('review')
		ratings = review
		min_value = int(request.POST.get('min_value'))
		max_value = int(request.POST.get('max_value'))
		
		availability = request.POST.get('availability')		
		colors = request.POST.getlist('colors')
		
		#return HttpResponse(ratings)
		
		all_products = Product.objects.all()
		filtered_products = set()
		for item in all_products:
			if item.price >=min_value and item.price <=max_value:
				filtered_products.add(item)

			for i, j in zip(colors, list(item.colors.all())):
				if i == j:
					filtered_products.add(item)
				else:
					pass
					
				
		for rating in ratings:
			rate_match_products = Product.objects.filter(rating=int(rating))
			for eachitem in rate_match_products:
				filtered_products.add(eachitem)
		#	product = get_object_or_404(Product, rating=rating)
		#	if product:
				#filtered_products.add(product)
			#else:
				#pass
				
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
				
		page_title = "Filtered Products"
		context = {"total_price": total_price, "product_quantitys": product_quantitys, "products": filtered_products, "page_title": page_title}
		return render(request, 'product/all_products.html', context)	

		
	else:
	
		bedroom_section = products = Product.objects.filter(category="BEDROOM")
		kitchen_dinning_section = Product.objects.filter(category="KITCHEN & DINNING")
		living_room_section = Product.objects.filter(category="LIVING ROOM")
		office_section = Product.objects.filter(category="OFFICE")
		kiddies_section = Product.objects.filter(category="KIDDIES")
		acessories_section = Product.objects.filter(category="ACESSORIES")
	
		section_one = Product.objects.all()[:6]
		section_two = Product.objects.all()[:6]
		section_three = Product.objects.all()[:6]
		all_products = Product.objects.all()
	
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
	
		context = {"total_price": total_price, "product_quantitys": product_quantitys, "section_one": section_one, "section_two": section_two, "section_three": section_three, "bedroom_section": bedroom_section, "all_products": all_products, "kitchen_dinning_section": kitchen_dinning_section, "living_room_section": living_room_section, "office_section": office_section, "kiddies_section": kiddies_section, "acessories_section": acessories_section}
		return render(request, 'main/shop.html', context)




def SearchView(request):
	context = {}
	return render(request, 'main/search.html', context)
	
	
	
def CheckoutView(request):
	user_id = request.user.id
	if request.method == "POST":
		full_name = request.POST.get("full_name")
		company_name = request.POST.get("company_name")
		email = request.POST.get("email")
		#password = request.POST.get("password")
		country = request.POST.get("country")
		phone = request.POST.get("phone")
		address = request.POST.get("address")
		order_note = request.POST.get("order_note")
		pub_date = timezone.now()
	
		customer = Customer.objects.create(full_name=full_name, company_name=company_name, email=email, country=country, phone=phone, address=address, order_note=order_note, pub_date=pub_date)
		customer.save()
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
			#total_quantity += int(str(item.quantity))
		
		
		cart.total_price = total_price
		cart.save()
		order = Order.objects.create(customer=customer, cart=cart,  pub_date=pub_date)
		order.save()
		#total_price = total_price * total_quantity
		
		
		
		#paystack comes in here
		#return HttpResponse("i got here moda fucker!")
		
		return HttpResponseRedirect(reverse("checkout_confirm", args=(order.id,)))
		
	else:
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
			
		if total_price == 0:
			return HttpResponseRedirect(reverse("shop"))
		elif total_price > 0:
			context = {"total_price": total_price, "cart": cart, "product_quantitys": product_quantitys, }
			return render(request, 'main/checkout.html', context)
		else:
			return HttpResponseRedirect(reverse("shop"))
		
		
def CheckoutConfirmView(request, order_id):
	order = get_object_or_404(Order, id=order_id, cart__user=request.user)
	
	#return HttpResponse(order.cart.total_price)
	context = {"order": order}
	return render(request, 'main/checkoutt.html', context)
	
def ConfirmOrderView(request, order_id):
	if request.method == "POST":
		status = "Confirmed"
		order = get_object_or_404(Order, id=order_id, cart__user=request.user)
		order.status = status	
		order.save()

		#here we reduce product quantity as planned
		cart = order.cart
		product_quantitys = cart.product_quantitys.all()
		for item in product_quantitys:
			product = Product.objects.get(slug=item.product.slug)
			product.quantity -= int(str(item.quantity))
			product.save()
		

		logout(request)
		return HttpResponseRedirect(reverse("index"))
		
	else:
		context = {}
		return render(request, 'main/confirm_order.html', context)
	
		
		 
def FaqsView(request):
	context = {}
	return render(request, 'main/faqs.html', context)
	
	

def RegisterLoginView(request):
	context = {}
	return render(request, 'main/register_login.html', context)	
	
	
	
def UserLogoutView(request):
	logout(request)
	return HttpResponseRedirect(reverse("index"))

	
	
def AboutView(request):
	context = {}
	return render(request, 'main/about.html', context)
