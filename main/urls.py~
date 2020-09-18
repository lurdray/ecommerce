from django.urls import path
from . import views

#app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),
	path("about/", views.AboutView, name="about"),
	
	path("category/<str:category>/", views.CategoryView, name="category"),
	path("shop/", views.ShopView, name="shop"),
	
	path("checkout/", views.CheckoutView, name="checkout"),
	path("checkout-confirm/<int:order_id>", views.CheckoutConfirmView, name="checkout_confirm"),
	path("checkout-confirm-order/<int:order_id>/", views.ConfirmOrderView, name="confirm_order"),
	
	path("faqs/", views.FaqsView, name="faqs"),
	path("privacy/", views.PrivacyView, name="privacy"),
	path("terms-and-condition/", views.TermsConditionView, name="termscondition"),
	path("shipping/", views.ShippingView, name="shipping"),
	path("affiliate/", views.AffiliateView, name="affiliate"),
	path("career/", views.CareerView, name="career"),
	path("contact/", views.ContactView, name="contact"),
	
	path("register-or-login/", views.RegisterLoginView, name="register_login"),
	
	path("search-result", views.SearchView, name="search"),

	path("userlogout/", views.UserLogoutView, name="userlogout"),
]
