# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from apps.authentication import views

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),


    #Tenant, Team, and User
    path('myteam/BJL192PPTTO92PP123PP/', views.myteam, name='myteam'),
    path('userprofile/BJL192PPTTO92PP123PP/', views.userprofile, name='userprofile'),
    # path('edit_profile/BJL192PPTTO92PP123PP/', views.edit_profile, name='edit_profile'),
    #path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('restaurant/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:pk>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/create/', views.restaurant_create, name='restaurant_create'),
    path('restaurant/<int:pk>/update/', views.restaurant_update, name='restaurant_update'),
    path('restaurant/<int:pk>/delete/', views.restaurant_delete, name='restaurant_delete'),
]
