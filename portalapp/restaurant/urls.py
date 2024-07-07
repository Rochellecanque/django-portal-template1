# restaurant/urls.py

#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.restaurant_list, name='restaurant-list'),
    path('<int:pk>/', views.restaurant_detail, name='restaurant-detail'),
    path('create/', views.restaurant_create, name='restaurant-create'),
    path('<int:pk>/update/', views.restaurant_update, name='restaurant-update'),
    path('<int:pk>/delete/', views.restaurant_delete, name='restaurant-delete'),
]
