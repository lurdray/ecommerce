from django.urls import path
from . import views

#app_name = "product"

urlpatterns = [

	path('add-customer/', views.AddCustomerView, name="add_customer"),
	path("all-customers/", views.AllCustomersView, name="all_customers"),
	path("customer/<slug:slug>/", views.CustomerDetailView, name="customer"),
	path("edit-customer/<slug:slug>/", views.EditCustomerView, name="edit_customer"),
	path("delete-customert/<slug:slug>/", views.DeleteCustomerView, name="delete_customer"),
	path("login/", views.LoginView, name="login"),

]
