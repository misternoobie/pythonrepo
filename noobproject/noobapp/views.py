from django.shortcuts import render
from django.contrib import messages
from .models import friend
from .forms import PostForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_list_or_404, get_object_or_404

# Create your views here.
def list_friends(request):
	object_list = friend.objects.all()
	context = {"object_list": object_list}
	return render(request,'friendslist.html', context)


#Create
def add_friend(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request,"Friend Successfully Added")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {"form":form,}
	return render(request,"add_friend.html", context)

def friend_detail(request, slug=None):
	instance = get_object_or_404(friend, slug=slug)
	context = {
		"name": instance.Name,
		"instance": instance
	}
	return render(request, "post_detail.html", context)

#def delete_friend(request):

#def update(request):