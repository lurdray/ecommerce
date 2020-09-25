from django.shortcuts import render, get_object_or_404
from poll.models import Poll, Option, Comment, PollCommentConnector
from customer.models import Customer
from cart.models import Cart
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

import random
import string
from django.db.models import Max, Min
from main.views import ray_randomiser
from django.utils import timezone

# Create your views here.
def AllPollView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'poll/all_poll.html', context)
		

	else:
		if request.user.is_active:
			user = request.user
			user = User.objects.get(id=user.id)
			user_checker = authenticate(username=user.username, password=user.password)
			#pass
			#return HttpResponse("issues ooo!")
		else:
			#return HttpResponse("i reached here ooo!")
			fake_username = "%s" % (ray_randomiser())
			fake_password = "%s" % (ray_randomiser())
			user = User.objects.create(username=fake_username)
			user.save()
			user.set_password(fake_password)
			user.save()
			user_checker = authenticate(username=fake_username, password=fake_password)
			
			if user.is_active:
				login(request, user_checker)
			else:
				pass

			cart = Cart.objects.create(user=user, pub_date=timezone.now())
			cart.user = user
			cart.save()
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))

		message = ""
		section_one = Poll.objects.order_by("-pub_date")[:5]
		section_two = Poll.objects.order_by("-pub_date")[5:10]
		section_three = Poll.objects.order_by("-pub_date")[5:15]

		section_box = [section_one, section_two]

		context ={"product_quantitys": product_quantitys, "total_price": total_price, "section_one": section_one, "section_two": section_two, "section_three": section_three, "section_box": section_box, "message": message}
		return render(request, 'poll/all_poll.html', context)



def PollDetailView(request, poll_id):
	poll = Poll.objects.get(id=poll_id)

	if request.method == "POST":
		if request.user.is_active:
			user = request.user
			user = User.objects.get(id=user.id)
			user_checker = authenticate(username=user.username, password=user.password)
			#pass
			#return HttpResponse("issues ooo!")
		else:
			#return HttpResponse("i reached here ooo!")
			fake_username = "%s" % (ray_randomiser())
			fake_password = "%s" % (ray_randomiser())
			user = User.objects.create(username=fake_username)
			user.save()
			user.set_password(fake_password)
			user.save()
			user_checker = authenticate(username=fake_username, password=fake_password)
			
			if user.is_active:
				login(request, user_checker)
			else:
				pass

			cart = Cart.objects.create(user=user, pub_date=timezone.now())
			cart.user = user
			cart.save()
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))

		if str(request.user.id) == str(poll.user_id):
			#return HttpResponse("iasaisas aisjiasas ")
			section_one = Poll.objects.order_by("-pub_date")[:5]
			section_two = Poll.objects.order_by("-pub_date")[5:10]
			section_three = Poll.objects.order_by("-pub_date")[5:15]
			message = "Sorry!, You have already reviewed that product."
			context ={"product_quantitys": product_quantitys, "total_price": total_price, "section_one": section_one, "section_two": section_two, "section_three": section_three, "message": message}
			return render(request, 'poll/all_poll.html', context)

		else:

			poll = Poll.objects.get(id=poll_id)
			poll.user_id = str(request.user.id)

			full_name = request.POST.get("full_name")
			email = request.POST.get("email")
			customer = Customer.objects.create(full_name=full_name, email=email)
			customer.save()
			poll.customer_id = customer.id
			poll.save()


			option = request.POST.get("option")
			opt = Option.objects.get(id=option)
			opt.vote += 1
			opt.save()

			#return HttpResponse(opt.vote)


			comment = request.POST.get("comment")
			com = Comment.objects.create(comment=comment)
			com.save()

			pc = PollCommentConnector(poll=poll, comment=com)
			pc.save()

			section_one = Poll.objects.order_by("-pub_date")[:5]
			section_two = Poll.objects.order_by("-pub_date")[5:10]
			section_three = Poll.objects.order_by("-pub_date")[5:15]
			message = "Review Sent!, Thank You for Voting!"
			context ={"product_quantitys": product_quantitys, "total_price": total_price, "section_one": section_one, "section_two": section_two, "section_three": section_three, "message": message}
			return render(request, 'poll/all_poll.html', context)

			#return HttpResponseRedirect(reverse("all_poll"))

			#context ={"poll": poll}
			#return render(request, 'poll/poll_detail.html', context)
		

	else:
		if request.user.is_active:
			user = request.user
			user = User.objects.get(id=user.id)
			user_checker = authenticate(username=user.username, password=user.password)
			#pass
			#return HttpResponse("issues ooo!")
		else:
			#return HttpResponse("i reached here ooo!")
			fake_username = "%s" % (ray_randomiser())
			fake_password = "%s" % (ray_randomiser())
			user = User.objects.create(username=fake_username)
			user.save()
			user.set_password(fake_password)
			user.save()
			user_checker = authenticate(username=fake_username, password=fake_password)
			
			if user.is_active:
				login(request, user_checker)
			else:
				pass

			cart = Cart.objects.create(user=user, pub_date=timezone.now())
			cart.user = user
			cart.save()
		
		cart = get_object_or_404(Cart, user__pk=request.user.id)
		product_quantitys = cart.product_quantitys.all()
		total_price = 0
		total_quantity = 0
		for item in product_quantitys:
			total_price += (item.product.price * int(str(item.quantity))) + (item.total_shipping_charge * int(str(item.quantity)))


		poll = Poll.objects.get(id=poll_id)
		options = poll.options.all()
		votes = []
		var_dict = {}
		total_votes = 0
		option_list = []
		option_listk = []
		for option in options:
			total_votes += option.vote

		for option in options:
			try:
				var = round((option.vote/total_votes) * 100)
			except:
				var = 0
			var_dict[option.option] = var
			option_list.append(var)
			option_listk.append(option.vote)

		try:
			highest_vote = max(option_list)
			highest_votek = max(option_listk)

		except:
			highest_vote = 0
			highest_votek = 0

		highest_options = poll.options.filter(vote=highest_votek)

		comments = poll.comments.all().order_by("-pub_date")[:5]
		section_one = Poll.objects.order_by("-pub_date")[:5]

		#return HttpResponse(str(poll.description))

		context ={"section_one": section_one, "total_price": total_price, "product_quantitys": product_quantitys, "poll": poll, "options": options, "votes": var_dict, "highest_vote": highest_vote, "highest_options": highest_options, "comments": comments}
		return render(request, 'poll/poll_detail.html', context)



def PollResultView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'poll/poll_result.html', context)
		

	else:
		context ={}
		return render(request, 'poll/poll_result.html', context)


