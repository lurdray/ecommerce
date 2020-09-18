from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
	name = models.CharField(max_length=150, default="none")
	email = models.CharField(max_length=150, default="none")
	review = models.TextField(default="none")
	status = models.CharField(max_length=150, default="pending")
	pub_date = models.DateTimeField(default=timezone.now)
	
	
	
	def __str__(self):
		return self.review
		

class Color(models.Model):
	color = models.TextField(default="none")
	
	def __str__(self):
		return self.color
		

class Product(models.Model):
	name = models.CharField(max_length=150)
	tag_title = models.CharField(max_length=150, default="Sale")
	tag_title_color = models.CharField(max_length=150, default="orange")
	section = models.CharField(max_length=150, default="section_one")
	image_1 = models.ImageField(upload_to='product/images/')
	image_2 = models.ImageField(upload_to='product/images/')
	image_3 = models.ImageField(upload_to='product/images/')
	image_4 = models.ImageField(upload_to='product/images/')
	video = models.CharField(max_length=150, default="jshsjssd7sjs")
	#image_5 = models.ImageField(upload_to='product/images/')
	description = models.TextField(default="none")
	specification = models.TextField(default="none")
	review = models.ManyToManyField(Review, through="ProductReviewConnector", through_fields=("product", "review"),)
	#review = models.TextField(default="none")
	category = models.CharField(max_length=150)
	quantity = models.IntegerField(blank=True, null=True)
	threshold = models.IntegerField(blank=True, null=True, default=1)
	price = models.IntegerField(blank=True, null=True)
	old_price = models.IntegerField(blank=True, null=True, default=0)
	rating = models.IntegerField(blank=True, null=True)
	colors = models.ManyToManyField(Color, through="ProductColorConnector", through_fields=("product", "color"),)
	shipping_charge = models.FloatField(blank=True, null=True)
	dimension = models.CharField(max_length=150)
	delivery_info = models.CharField(max_length=150, default="none")
	slug = models.SlugField(unique=True, default="rayslug")
	pub_date = models.DateTimeField(default=timezone.now)
	
	def save(self, *args, **kwargs):
		var = self.name + "/" + str(self.pub_date)
		self.slug = slugify(var)
		super().save(*args, **kwargs)
		
	def get_absolute_url(self):
		return "/product-detail/%s/"%self.slug
		
	def __str__(self):
		return self.name
		

class Quantity(models.Model):
	quantity = models.IntegerField(blank=True, null=True)

	def __str__(self):
		#never forget that _str_ function should never return an int
		return str(self.quantity)		
		
class ProductQuantity(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
	quantity = models.ForeignKey(Quantity, on_delete=models.CASCADE)
	total_shipping_charge = models.IntegerField(blank=True, null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	
	def __str__(self):
		return str(self.product.name)		
	
		
	
class ProductReviewConnector(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
	review = models.ForeignKey(Review, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)
	
	
class ProductColorConnector(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, default="")
	color = models.ForeignKey(Color, on_delete=models.CASCADE, default="")
	pub_date = models.DateTimeField(default=timezone.now)

