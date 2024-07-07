# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from core.models import Profile


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


# class EditProfileForm(forms.ModelForm):
#     email = forms.EmailField(
#         widget=forms.EmailInput(
#             attrs={
#                 "placeholder": "Email",
#                 "class": "form-control"
#             }
#         ))
#     first_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "First Name",
#                 "class": "form-control"
#             }
#         ))
#     last_name = forms.CharField(
#         max_length=30,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Last Name",
#                 "class": "form-control"
#             }
#         ))
#     address = forms.CharField(
#         max_length=255,
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Address",
#                 "class": "form-control"
#             }
#         ))
#     city = forms.CharField(
#         max_length=100,
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "City",
#                 "class": "form-control"
#             }
#         ))
#     country = forms.CharField(
#         max_length=100,
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Country",
#                 "class": "form-control"
#             }
#         ))
#     postal_code = forms.CharField(
#         max_length=20,
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 "placeholder": "Postal Code",
#                 "class": "form-control"
#             }
#         ))
#     about_me = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 "placeholder": "About Me",
#                 "class": "form-control"
#             }
#         ),
#         required=False
#     )

#     class Meta:
#         model = Profile
#         fields = ('email', 'first_name', 'last_name', 'address', 'city', 'country', 'postal_code', 'about_me')