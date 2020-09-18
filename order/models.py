from django.db import models
from cart.models import Cart
from customer.models import Customer
from django.utils import timezone

# Create your models here.
class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
	cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default="")
	status = models.CharField(max_length=150, default="Pending")
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.customer.full_name
	
	
