from django.shortcuts import render
from order.models import Order
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy

# Create your views here.
def AddOrderView(request, cart_id):
	cart = get_object_or_404(Cart, user__pk=request.user.id, id=cart_id)
	order = Order.object.create(pub_date=pub_date, cart=cart)
	context = {}
	return render(request, 'order/add_order.html', context)
	
def OrderDetailView(request, order_id):
	context = {}
	return render(request, 'order/order_detail.html', context)

def AllOrdersView(request):
	orders = Order.objects.order_by("-pub_date")
	context = {"orders": orders}
	return render(request, 'order/all_orders.html', context)
	
def DeleteOrderView(request, order_id):
	order = Order.objects.get(id=order_id)
	order.delete()
		
	return HttpResponseRedirect(reverse("all_orders"))
	
