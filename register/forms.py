from django import forms

from .models import User

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        password = forms.CharField(widget=forms.PasswordInput)
        fields = ('first_name', 'last_name', 'email', 'password',)
        widgets = {
            'password': forms.PasswordInput(),
        }