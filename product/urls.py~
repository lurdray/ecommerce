from django.urls import path
from . import views

#app_name = "product"

urlpatterns = [

	path('add-product/', views.AddProductView, name="add_product"),
	path("all-products/", views.AllProductsView, name="all_products"),
	path("product-detail/<slug:slug>/", views.ProductDetailView, name="product_detail"),
	path("edit-product/<slug:slug>/", views.EditProductView, name="edit_product"),
	path("delete-product/<slug:slug>/", views.DeleteProductView, name="delete_product"),
	
]
