# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.sample import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('restaurant/', views.pages, name='restaurant'),  # Ensure this maps correctly

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
