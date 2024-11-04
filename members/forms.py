from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    first_name = forms.CharField(max_length=100, widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'First name'}))
    last_name = forms.CharField(max_length=100,  widget = forms.TextInput(attrs={'class': 'form-control','placeholder':'Last name'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'