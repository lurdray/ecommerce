from django.urls import path
from . import views

#app_name = "product"

urlpatterns = [

	path('add-order-from-cart/<int:cart_id>/', views.AddOrderView, name="add_order"),
	path("all-orders/", views.AllOrdersView, name="all_orders"),
	path("order/<int:order_id>/", views.OrderDetailView, name="order_detail"),
	#path("edit-order/<int:order_id>/", views.EditOrderView, name="edit_order"),
	path("delete-order/<int:order_id>/", views.DeleteOrderView, name="delete_order"),

]
