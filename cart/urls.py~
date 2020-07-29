from django.urls import path
from . import views

#app_name = "product"

urlpatterns = [

	path('add-product-to-cart/<slug:slug>/', views.AddProductCartView, name="add_product_to_cart"),
	path("remove-product-from-cart/<slug:slug>/", views.RemoveProductCartView, name="remove_product_cart"),
	path("all-carts/", views.AllCartsView, name="all_carts"),
	path("cart/<int:user_id>/", views.CartView, name="cart"),
	path("edit-cart/<int:card_id>/", views.EditCartView, name="edit_cart"),
	path("delete-cart/<int:card_id>/", views.DeleteCartView, name="delete_cart"),

]
