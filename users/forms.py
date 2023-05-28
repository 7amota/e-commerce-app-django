from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User
class UserRegister(UserCreationForm):
     email = forms.EmailField(required=True)
     password1 = forms.CharField(widget=forms.PasswordInput)
     password2 = forms.CharField(widget=forms.PasswordInput)
     class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserLogin(forms.ModelForm):
   email = forms.EmailField(label='Email' ,required=True)
   password = forms.CharField(label='Password' ,widget = forms.PasswordInput)
   class Meta:
      model = User
      fields = ['email','password']
   