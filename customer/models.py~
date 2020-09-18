from django.db import models
from product.models import Product
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
	full_name = models.CharField(max_length=150, default="none")
	company_name = models.CharField(max_length=150, default="none")
	email = models.CharField(max_length=150, default="none")
	password = models.CharField(max_length=150, default="none")
	country = models.CharField(max_length=150, default="none")
	phone = models.CharField(max_length=150, default="none")
	address = models.CharField(max_length=150, default="none")
	order_note = models.CharField(max_length=150, default="none")
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	def __str__(self):
		return self.full_name
		
		
class WishList(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default="")
	products = models.ManyToManyField(Product, through="WishListProductConnector", through_fields=("wishlist", "product"),)
	pub_date = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.customer.full_name
		
		
		
class WishListProductConnector(models.Model):
	wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE, default="")
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)
