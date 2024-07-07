# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.decorators import login_required

#Load CORE views to inherit from
from core import views as CORE_VIEWS
from restaurant import views as Restaurant_VIEWS
from restaurant.models import Restaurant
from restaurant.forms import RestaurantForm 

#from .forms import EditProfileForm  

def login_view(request):
    context = CORE_VIEWS.context_maker(request, {})

    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    context['form'] = form
    context['msg'] = msg

    return render(request, "authentication/login.html", context)


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "authentication/register.html", {"form": form, "msg": msg, "success": success})

@login_required(login_url="/login/")
def myteam (request):
    context = CORE_VIEWS.context_maker(request, {})
    return render(request, "authentication/myteam.html", context)

@login_required(login_url="/login/")
def userprofile (request):
    context = CORE_VIEWS.context_maker(request, {})
    return CORE_VIEWS.template_loader(request, context, 'authentication/profile.html')

# @login_required(login_url="/login/")
# def edit_profile (request):
#     context = CORE_VIEWS.context_maker(request, {})
#     return CORE_VIEWS.template_loader(request, context, 'authentication/edit_profile.html')


# @login_required
# def edit_profile(request):
#     profile = request.user.profile
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Your profile has been updated successfully.')
#             return redirect('userprofile')  # Adjust this to your profile view URL
#     else:
#         form = EditProfileForm(instance=profile)
    
#     context = {
#         'form': form
#     }
#     return render(request, 'authentication/edit_profile.html', context)


#### Restaurant

@login_required(login_url="/restaurant/")
def restaurant_list (request):
    return Restaurant_VIEWS.restaurant_list(request)

@login_required(login_url="/login/")
def restaurant_detail(request, pk):
    return Restaurant_VIEWS.restaurant_detail(request, pk)

@login_required(login_url="/login/")
def restaurant_create(request):
    context = CORE_VIEWS.context_maker(request, {})
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant')
    else:
        form = RestaurantForm()
    context['form'] = form
    return render(request, 'restaurant/restaurant_form.html', context)


@login_required(login_url="/login/")
def restaurant_update(request, pk):
    context = CORE_VIEWS.context_maker(request, {})
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)
    context['form'] = form
    return render(request, 'restaurant/restaurant_form.html', context)


@login_required(login_url="/login/")
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant')
    return render(request, 'restaurant/restaurant_confirm_delete.html', {'restaurant': restaurant})