from django import forms
from django.contrib.auth.forms import UserCreationForm

from homeapp.models import Login, userpage, workerpage


class LoginRegister(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2')

class userform(forms.ModelForm):
    class Meta:
        model=userpage
        exclude=('user',)

class workerform(forms.ModelForm):
    class Meta:
        model=workerpage
        exclude=('user',)


