from product.models import Product, ProductQuantity, Quantity, ProductColorConnector, ProductReviewConnector, Review
from cart.models import CartProductQuantityConnector, Cart
from shipping.views import GetDistance
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from main.views import ray_randomiser 


# Create your views here.
def AddProductView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		tag_title = request.POST.get("tag_title")
		tag_title_color = request.POST.get("tag_title_color")
		section = request.POST.get("section")
		description = request.POST.get("description")
		specification = request.POST.get("specification")
		category = request.POST.get("category")
		quantity = request.POST.get("quantity")
		threshold = request.POST.get("threshold")
		price = request.POST.get("price")
		old_price = request.POST.get("old_price")
		rating = request.POST.get("rating")
		colors = request.POST.getlist('colors')
		shipping_charge = request.POST.get("shipping_charge")
		dimension = request.POST.get("dimension")
		delivery_info = request.POST.get("delivery_info")
		
		
		video_link = request.POST.get("video")
		
		video = str("https://youtube.com/embed/" + video_link)


		pub_date = timezone.now()

		product = Product.objects.create(name=name, tag_title=tag_title, tag_title_color=tag_title_color, section=section, description=description, specification=specification, category=category, quantity=quantity, threshold=threshold, price=price, old_price=old_price, rating=rating, shipping_charge=shipping_charge, dimension=dimension, delivery_info=delivery_info, slug=name, video=video, pub_date=pub_date)
		try:
			if request.FILES["image_1"]:
				image_1 = request.FILES["image_1"]
				product.image_1 = image_1
			if request.FILES["image_2"]:
				image_2 = request.FILES["image_2"]
				product.image_2 = image_2
			if request.FILES["image_3"]:
				image_3 = request.FILES["image_3"]
				product.image_3 = image_3
			if request.FILES["image_4"]:
				image_4 = request.FILES["image_4"]
				product.image_4 = image_4
			if request.FILES["image_5"]:
				image_5 = request.FILES["image_5"]
				product.image_5 = image_5

			else:
				pass

		except:
			pass
		product.save()
		
		for item in colors:
			pc = ProductColorConnector(product=product, color=item, pub_date=pub_date)
			pc.save()		
		
			
		return HttpResponseRedirect(reverse("dashboard_all_products"))
		
	else:
		context = {}
		return render(request, 'product/add_product.html', context)
		
	


	
	
def ProductDetailView(request, slug):
	if request.method == "POST":
		product = get_object_or_404(Product, slug=slug)
		name = ""
		review = ""
		name = request.POST.get('name')
		email = request.POST.get('email')
		review = request.POST.get('review')
		
		if name == None:
			#return HttpResponse(name)
			quantity_k = int(str(request.POST.get("quantity")))
			quantity = Quantity.objects.create(quantity=quantity_k)
			quantity.save()
		
			user_id = request.user.id
			pub_date = timezone.now()
		
			cart = get_object_or_404(Cart, user__pk=user_id)
			product = get_object_or_404(Product, slug=slug)
		
			#var = "%s, %s" % (product.quantityhgfrxcv, quantity)
			#return HttpResponse(var)
			#code for checking if the customer orders more than the available quantity
			if quantity_k > product.quantity:
				messages.success(request, "Sorry, There are not enough amout of this product.")
				return HttpResponseRedirect(reverse("all_products"))
	
			else:
				product.quantity -= quantity_k
				product.save()
				distance = GetDistance()
				total_shipping_charge = (product.shipping_charge * distance)
				product_quantity = ProductQuantity.objects.create(product=product, quantity=quantity, total_shipping_charge=total_shipping_charge)
				product_quantity.save()
		
				cp = CartProductQuantityConnector(cart=cart, product_quantity=product_quantity, pub_date=pub_date)
				cp.save()
				messages.success(request, "Product Successfully Added to Cart")
		
				return HttpResponseRedirect(reverse("all_products"))
				
		else:
			#return HttpResponse(name)
			review = Review.objects.create(name=name, email=email, review=review)
			review.save()
			pc = ProductReviewConnector(product=product, review=review)
			pc.save()
			
			cart = get_object_or_404(Cart, user__pk=request.user.id)
			product_quantitys = cart.product_quantitys.all()
			total_price = 0
			total_quantity = 0
			for item in product_quantitys:
				total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))
	
			product = Product.objects.get(slug=slug)
			section_one = Product.objects.filter(section="section_one").order_by("-pub_date")[:1]
			section_two = Product.objects.filter(section="section_two").order_by("-pub_date")[:10]
			section_three = Product.objects.filter(section="section_three").order_by("-pub_date")[:10]
			related_products = Product.objects.filter(section=product.section).order_by("-pub_date")[:10]
			all_products = Product.objects.all()
			
			context = {"total_price": total_price, "product_quantitys": product_quantitys, "product": product, "section_one": section_one, "section_two": section_two, "section_three": section_three, "all_products": all_products}
			messages.success(request, "Review Submitted Successfully!")
			return render(request, 'product/product_detail.html', context)
			

	else:
		#distance = GetDistance()
		#return HttpResponse(distance)
		
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
			total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))
	
		product = Product.objects.get(slug=slug)
		section_one = Product.objects.filter(section="section_one").order_by("-pub_date")[:2]
		section_two = Product.objects.filter(section="section_two").order_by("-pub_date")[:10]
		section_three = Product.objects.filter(section="section_three").order_by("-pub_date")[:10]
		related_products = Product.objects.filter(section=product.section).order_by("-pub_date")[:10]

		all_products = Product.objects.all()
		context = {"related_products": related_products, "total_price": total_price, "product_quantitys": product_quantitys, "product": product, "section_one": section_one, "section_two": section_two, "section_three": section_three, "all_products": all_products}
		
		return render(request, 'product/product_detail.html', context)
	
	
	

def EditProductView(request, slug):
	if request.method == "POST":
		name = request.POST.get("name")
		tag_title = request.POST.get("tag_title")
		tag_title_color = request.POST.get("tag_title_color")
		section = request.POST.get("section")
		description = request.POST.get("description")
		specification = request.POST.get("specification")
		quantity = request.POST.get("quantity")
		price = request.POST.get("price")
		shipping_charge = request.POST.get("shipping_charge")
		dimension = request.POST.get("dimension")
		delivery_info = request.POST.get("delivery_info")
		
		video = request.POST.get("video")
		
		product = Product.objects.filter(slug=slug)
		product.update(name=name, tag_title=tag_title, tag_title_color=tag_title_color, section=section, description=description, specification=specification, quantity=quantity, price=price, shipping_charge=shipping_charge, dimension=dimension, delivery_info=delivery_info, video=video)
		
		return HttpResponseRedirect(reverse("dashboard_all_products"))
		
		
		
	else:
		product = Product.objects.get(slug=slug)
		context = {"product": product}
		return render(request, 'product/edit_product.html', context)
	

def DeleteProductView(request, slug):
	product = Product.objects.get(slug=slug)
	product.delete()
		
	return HttpResponseRedirect(reverse("dashboard_all_products"))
	
def AllProductsView(request):
	if request.method == "POST":
		query = request.POST.get('query')
		category = request.POST.get('category')
		products = Product.objects.filter(name__icontains=query, category=category)
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))
			
		context = {"total_price": total_price, "product_quantitys": product_quantitys, 'products': products}
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
			total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))
		
		page_title = "All Products"
		products = Product.objects.order_by("-pub_date")
	
	
		context = {"total_price": total_price, "product_quantitys": product_quantitys, "products": products, "page_title": page_title}
		return render(request, 'product/all_products.html', context)
