from django.urls import path
from . import views

#app_name = "main"

urlpatterns = [

	#path("", views.IndexView, name="index"),
	path("dashboard/", views.DashboardView, name="dashboard"),
	path("dashboard-product-detail/<slug:slug>", views.DashboardProductDetailView, name="dashboard_product_detail"),
	path("dashboard-order-detail/<int:order_id>/", views.DashboardOrderDetailView, name="dashboard_order_detail"),
	path("dashboard-customer-detail/<int:customer_id>", views.DashboardCustomerDetailView, name="dashboard_customer_detail"),
	path("dashboard-all-products/", views.DashboardAllProductsView, name="dashboard_all_products"),
	path("dashboard-all-reviews/", views.DashboardAllReviewsView, name="dashboard_all_reviews"),
	path("dashboard-logout/", views.DashboardLogoutView, name="dashboard_logout"),

	########polls shit
	path('add-poll/', views.AddPollView, name="add_poll"),
	path('edit-poll/', views.EditPollView, name="edit_detail"),
	path('delete-poll/', views.DeletePollView, name="delete_poll"),
	path('all-poll/', views.AllPollView, name="all_poll"),
	path('poll-detail/', views.PollDetailView, name="poll_detail"),
	path('poll-result/', views.PollResultView, name="poll_result"),

]
