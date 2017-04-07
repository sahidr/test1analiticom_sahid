from django.shortcuts import render
from .models import User
from django.shortcuts import render, get_object_or_404
from .forms import UserForm
from django.shortcuts import redirect

# Create your views here.
def user_list(request):
	users = User.objects.all()
	return render(request, 'register/user_list.html', {'users': users})

def user_detail(request, pk):
	user = get_object_or_404(User, pk=pk)
	return render(request, 'register/user_detail.html', {'user': user})

def user_new(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('user_list')
	else:
		form = UserForm()
		return render(request, 'register/user_edit.html', {'form': form})

def user_edit(request, pk):
	user = get_object_or_404(User, pk=pk)
	if request.method == "POST":
		form = UserForm(request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('user_detail', pk=user.pk)
	else:
		form = UserForm(instance=user)
		return render(request, 'register/user_edit.html', {'form': form})
