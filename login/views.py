# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
from .models import User
from django.utils import timezone
from django.shortcuts import redirect
from .forms import UserForm
# Create your views here.

def get_queryset(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
	# create a form instance and populate it with data from the request:
		form = User(request.POST)
	# check whether it's valid:
		if form.is_valid():
		# process the data in form.cleaned_data as required
		# ...
		# redirect to a new URL:
			return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = User()

	return render(request, 'registro.html', {'form': form})


def user_new(request,pk):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.first_name = request.first_name
			user.last_name = request.last_name
			user.email =request.email
			user.password = request.password
			user.save()
			return redirect('user_detail', pk=pk)
	else:
		#form = User.objects.get(pk=pk)
		form = UserForm(instance=form)
		return render(request, 'signup/index.html', {'form': form})

def user_list(request):
	users = User.objects.all()
	return render(request, 'signup/user_list.html', {'users': users})

def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'signup/user_detail.html', {'user': user})