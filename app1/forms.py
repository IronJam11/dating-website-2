from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms 
from django.forms.widgets import PasswordInput, TextInput
from .models import UserChoices

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
    

class ChoicesForm(forms.ModelForm):
     
     class Meta:
        model=UserChoices
        fields = ['gender','username','user1','user2','user3','enrollment_number','bio','branch', 'status', 'userphoto','user']
        def __init__(self, *args, **kwargs):
            super(ChoicesForm, self).__init__(*args, **kwargs)
            # Customize labels for specific fields
            self.fields['user'].label = 'Best Friend'
            
    
