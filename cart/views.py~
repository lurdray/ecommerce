from django.shortcuts import render
from cart.models import CartProductQuantityConnector, Cart
from product.models import Product, ProductQuantity, Quantity
from shipping.views import GetDistance
from django.contrib import messages 
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def AddProductCartView(request, slug):
	quantity = 1
	quantity = Quantity.objects.create(quantity=quantity)
	quantity.save()
		
	user_id = request.user.id
	pub_date = timezone.now()
		
	cart = get_object_or_404(Cart, user__pk=user_id)
	product = get_object_or_404(Product, slug=slug)
	
	#code for checking if the customer orders more than the available quantity
	if product.quantity < 1:
		return HttpResponse("Sorry, There are not enough amout of this product.")
	
	else:
		distance = GetDistance()
		total_shipping_charge = product.shipping_charge * distance

		product_quantity = ProductQuantity.objects.create(product=product, quantity=quantity, total_shipping_charge=total_shipping_charge)
		product_quantity.save()
		
		cp = CartProductQuantityConnector(cart=cart, product_quantity=product_quantity, pub_date=pub_date)
		cp.save()
		messages.success(request, "Product Successfully Added to Cart")
	
		return HttpResponseRedirect(reverse("category", args=(product.category,)))
	#pass
	#return HttpResponse(slug)
	#if request.user.is_active:
	#	if request.method == "POST":
	#		quantity = request.POST.get("quantity")
	#		return HttpResponse(quantity)
	#		cart = get_object_or_404(Cart, user__pk=request.user.id)
	#		product = get_object_or_404(Product, slug=slug)
	#		pub_date = timezone.now()
	#		cp = CartProductConnector(cart=cart, product=product, pub_date=pub_date)
	#		cp.save()
		
		
	#	quantity = request.POST.get("quantity")
	#	return HttpResponse(quantity)
	
	#	return HttpResponseRedirect(reverse("all_products"))
		
	#else:
	#	return HttpResponse("session expired!")
	
	
def CartView(request, user_id):
	if request.method == "POST":
		query = request.POST.get('query')
		category = request.POST.get('category')
		products = Product.objects.filter(name__icontains=query, category=category)
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity)))
			
		context = {"total_price": total_price, "product_quantitys": product_quantitys, 'products': products}
		return render(request, 'product/all_products.html', context)
		
	else:
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			qty = int(str(item.quantity))
			total_price += (item.product.price * qty) + (item.total_shipping_charge * qty)
			#add shipping charge 
			#
			#
	
		section_two = Product.objects.all()[:6]
		context = {"total_price": total_price, "product_quantitys": product_quantitys, "cart": cart, "section_two": section_two}
		return render(request, 'cart/cart.html', context)
	
	
############################################################################
def RemoveProductCartView(request, slug):
	cart = get_object_or_404(Cart, user__pk=request.user.id)
	product_quantitys = cart.product_quantitys.all()
	for item in product_quantitys:
		if item.product.slug == slug:
			product = get_object_or_404(Product, slug=slug)
			product_quantity = get_object_or_404(ProductQuantity, quantity=item.quantity, product=product)
			product_quantity.delete()
			cart.save()
		else:
			pass
			
	return HttpResponseRedirect(reverse("cart", args=(request.user.id,)))
	#return HttpResponseRedirect(reverse("cart"), args=(request.user.id))
##############################################################################				
	
	
def EditCartView(request):
	pass
	
def DeleteCartView(request):
	pass
	
	
def AllCartsView(request):
	pass
	
	

