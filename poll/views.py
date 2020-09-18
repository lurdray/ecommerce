from django.shortcuts import render

# Create your views here.
def AllPollView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'poll/all_poll.html', context)
		

	else:
		context ={}
		return render(request, 'poll/all_poll.html', context)



def PollDetailView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'poll/poll_detail.html', context)
		

	else:
		context ={}
		return render(request, 'poll/poll_detail.html', context)



def PollResultView(request):
	if request.method == "POST":
		context = {}
		return render(request, 'poll/poll_result.html', context)
		

	else:
		context ={}
		return render(request, 'poll/poll_result.html', context)


