from product.models import Product, ProductQuantity, Quantity, ProductColorConnector
from cart.models import CartProductQuantityConnector, Cart
from shipping.views import GetDistance
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy


# Create your views here.
def AddProductView(request):
	if request.method == "POST":
		name = request.POST.get("name")
		description = request.POST.get("description")
		specification = request.POST.get("specification")
		category = request.POST.get("category")
		quantity = request.POST.get("quantity")
		threshold = request.POST.get("threshold")
		price = request.POST.get("price")
		rating = request.POST.get("rating")
		colors = request.POST.getlist('colors')
		shipping_charge = request.POST.get("shipping_charge")
		dimension = request.POST.get("dimension")
		delivery_info = request.POST.get("delivery_info")
		
		image_1 = request.FILES["image_1"]
		image_2 = request.FILES["image_2"]
		image_3 = request.FILES["image_3"]
		image_4 = request.FILES["image_4"]
		#image_5 = request.FILES["image_5"]
		

		pub_date = timezone.now()


		product = Product.objects.create(name=name, image_1=image_1, image_2=image_2, image_3=image_3, image_4=image_4, description=description, specification=specification, category=category, quantity=quantity, threshold=threshold, price=price, rating=rating, shipping_charge=shipping_charge, dimension=dimension, delivery_info=delivery_info, slug=name, pub_date=pub_date)
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
		quantity_k = int(str(request.POST.get("quantity")))
		quantity = Quantity.objects.create(quantity=quantity_k)
		quantity.save()
		
		user_id = request.user.id
		pub_date = timezone.now()
		
		cart = get_object_or_404(Cart, user__pk=user_id)
		product = get_object_or_404(Product, slug=slug)
		
		#var = "%s, %s" % (product.quantity, quantity)
		#return HttpResponse(var)
		#code for checking if the customer orders more than the available quantity
		if quantity_k > product.quantity:
			return HttpResponse("Sorry, There are not enough amout of this product.")
	
		else:	
			distance = GetDistance()
			total_shipping_charge = (product.shipping_charge * distance)
			product_quantity = ProductQuantity.objects.create(product=product, quantity=quantity, total_shipping_charge=total_shipping_charge)
			product_quantity.save()
		
			cp = CartProductQuantityConnector(cart=cart, product_quantity=product_quantity, pub_date=pub_date)
			cp.save()
		
			return HttpResponseRedirect(reverse("all_products"))
			

	else:
		#distance = GetDistance()
		#return HttpResponse(distance)
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
	
		product = Product.objects.get(slug=slug)
		section_one = Product.objects.all()[:2]
		section_two = Product.objects.all()[:6]
		section_three = Product.objects.all()[:6]
		all_products = Product.objects.all()
		context = {"total_price": total_price, "product_quantitys": product_quantitys, "product": product, "section_one": section_one, "section_two": section_two, "section_three": section_three, "all_products": all_products}
		
		return render(request, 'product/product_detail.html', context)
	
	
	

def EditProductView(request, slug):
	if request.method == "POST":
		name = request.POST.get("name")
		description = request.POST.get("description")
		specification = request.POST.get("specification")
		quantity = request.POST.get("quantity")
		price = request.POST.get("price")
		shipping_charge = request.POST.get("shipping_charge")
		dimension = request.POST.get("dimension")
		delivery_info = request.POST.get("delivery_info")
		
		product = Product.objects.filter(slug=slug)
		product.update(name=name, description=description, specification=specification, quantity=quantity, price=price, shipping_charge=shipping_charge, dimension=dimension, delivery_info=delivery_info)
		
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
	cart = get_object_or_404(Cart, user__pk=request.user.id)
	product_quantitys = cart.product_quantitys.all()
	total_price = 0
	total_quantity = 0
	for item in product_quantitys:
		total_price += (item.product.price * int(str(item.quantity)))
		
	page_title = "All Products"
	products = Product.objects.order_by("-pub_date")
	context = {"total_price": total_price, "product_quantitys": product_quantitys, "products": products, "page_title": page_title}
	return render(request, 'product/all_products.html', context)
