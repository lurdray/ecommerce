from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from product.models import Product


class StaticViewSitemap(Sitemap):
	changefreq = "always"
	
	def items(self):
		return ["index", "about"]
		
	def location(self, item):
		return reverse(item)


class ProductSitemap(Sitemap):
	
	def items(self):
		return Product.objects.all()

