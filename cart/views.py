from django.shortcuts import render
from cart.models import CartProductQuantityConnector, Cart
from product.models import Product, ProductQuantity, Quantity
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def AddProductCartView(request, slug):
	quantity = 1
	quantity = Quantity.objects.create(quantity=quantity)
	quantity.save()
		
	user_id = request.user.id
	pub_date = timezone.now()
		
	cart = get_object_or_404(Cart, user__pk=user_id)
	product = get_object_or_404(Product, slug=slug)
		
	product_quantity = ProductQuantity.objects.create(product=product, quantity=quantity)
	product_quantity.save()
		
	cp = CartProductQuantityConnector(cart=cart, product_quantity=product_quantity, pub_date=pub_date)
	cp.save()
	
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
	cart = get_object_or_404(Cart, user__pk=request.user.id)
	product_quantitys = cart.product_quantitys.all()
	total_price = 0
	total_quantity = 0
	for item in product_quantitys:
		total_price += (item.product.price * int(str(item.quantity)))
	
	context = {"total_price": total_price, "product_quantitys": product_quantitys, "cart": cart}
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
	
	

