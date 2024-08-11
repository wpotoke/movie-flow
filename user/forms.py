# from django_recaptcha.fields import ReCaptchaField
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from user.models import User


class UserLoginForm(AuthenticationForm):

    # recaptcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ["username", "password", "rememder_me"]

    username = forms.CharField()
    password = forms.CharField()
    
    remember_me = forms.BooleanField(required=False)

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField()
    password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["username", "image", "email"]

    image = forms.ImageField(required=False)
    username = forms.CharField()
    email = forms.EmailField()

