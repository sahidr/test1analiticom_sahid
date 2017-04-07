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

class IndexView(generic.ListView):
	template_name = 'signup/index.html'
	context_object_name = 'user_new'

	def get_queryset(self):
		"""
		Return the last five published questions (not including those set to be
		published in the future).
		"""
		return User.objects.all()

	def register(request):
		if request.method == "POST":
			form = User(request.POST) # filled form/i'm skipping validation for this example
			return HttpResponseRedirect('/templates/signup/success.html') # go to some other page if successfully saved
		else:
			form = User# if the user accessed the register url directly, just display the empty form
			return render(request, 'signup/success.html',  {'form': form})

	def get_name(request):
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

	def index(request, pk):
		users = User.objects.get(pk=pk)
		return render(request, 'signup/index.html', { 'users': users })


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

class ListView(generic.ListView):
	template_name = 'signup/user_list.html'
	context_object_name = 'user_list'

	def user_list(request):
		users = User.objects.all()
		return render(request, 'signup/user_list.html', {'users': users})

class DetailView(generic.ListView):
	template_name = 'signup/user_detail.html'
	context_object_name = 'user_detail'

	def user_detail(request, pk):
		user = get_object_or_404(User, pk=pk)
		return render(request, 'signup/user_detail.html', {'user': user})