from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *

#  USER CREATION FORM
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


# ------------ ----- SIGNUP FORM PART ---------------------


# class RegisterForm(forms.ModelForm):
#     phone = forms.IntegerField(required=True)
#     password = forms.CharField(widget=forms.PasswordInput())
#     country_code = forms.IntegerField()
#     fullname = forms.CharField(max_length=50)
#     email = forms.EmailField()

#     MIN_LENGTH = 4

#     class Meta:
#         model = CustomUser
#         fields = ["email", "country_code", "phone", "password", "fullname"]

#     def clean_phone_number(self):
#         phone = self.data.get("phone")
#         if CustomUser.objects.filter(phone=phone).exists():
#             raise forms.ValidationError(
#                 _("Another user with this phone number already exists")
#             )
#         return phone

#     def clean_email(self):
#         email = self.data.get("email")
#         if CustomUser.objects.filter(email__iexact=email).exists():
#             raise forms.ValidationError("Email addresses must be unique.")
#         return email

#     def save(self, *args, **kwargs):
#         user = super(RegisterForm, self).save(*args, **kwargs)
#         user.set_password(self.cleaned_data["password"])
#         print("Saving user with country_code", user.country_code)
#         user.save()
#         return user


# # ------------ ----- LOGIN FORM PART ---------------------


# class LoginForm(forms.Form):
#     email = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput())

#     class Meta:
#         model = CustomUser
#         fields = ["email", "password"]



