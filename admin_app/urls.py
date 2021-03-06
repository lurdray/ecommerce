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
	path('dashboard-add-poll/', views.AddPollView, name="dashboard_add_poll"),
	path('dashboard-add-poll-option/<int:poll_id>/', views.AddOptionPollView, name="dashboard_add_poll_option"),
	path('dashboard-edit-poll/', views.EditPollView, name="dashboard_edit_detail"),
	path('dashboard-delete-poll/', views.DeletePollView, name="dashboard_delete_poll"),
	path('dashboard-all-poll/', views.AllPollView, name="dashboard_all_poll"),
	path('dashboard-poll-detail/<int:poll_id>/', views.PollDetailView, name="dashboard_poll_detail"),
	path('dashboard-poll-result/', views.PollResultView, name="dashboard_poll_result"),

]
