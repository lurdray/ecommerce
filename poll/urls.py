from django.urls import path
from . import views

#app_name = "product"

urlpatterns = [
	path('all-poll/', views.AllPollView, name="all_poll"),
	path('poll-detail/', views.PollDetailView, name="poll_detail"),
	path('poll-result/', views.PollResultView, name="poll_result"),


]
