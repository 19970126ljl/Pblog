from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

class infoform(UserChangeForm):
    """infoform definition."""
    head = forms.ImageField(required=False)
    gender = forms.BooleanField(required=False)
    class Meta:
        model = User
        fields = ('username','password','email','head')


