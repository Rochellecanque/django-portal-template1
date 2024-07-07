# restaurant/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm
from django.contrib.auth.decorators import login_required
from django.template import loader

# @login_required
# def restaurant_list(request):
#     print("Accessing restaurant_list view")
#     logger.debug("Accessing restaurant_list view")
#     restaurants = Restaurant.objects.all()
#     return render(request, 'restaurant/restaurant_list.html', {})

@login_required
def restaurant_list(request):
    print("Entering restaurant_list view")  # Print statement to indicate entry into the view
    restaurants = Restaurant.objects.all()
    print("Retrieved {} restaurants".format(len(restaurants)))  # Print statement to show number of restaurants retrieved
    return render(request, 'restaurant/restaurant_list.html', {'restaurants': restaurants})

def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurant/restaurant_detail.html', {'restaurant': restaurant})

@login_required
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant/restaurant_form.html', {'form': form})

@login_required
def restaurant_update(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant-detail', pk=pk)
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant/restaurant_form.html', {'form': form})

@login_required
def restaurant_delete(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant-list')
    return render(request, 'restaurant/restaurant_confirm_delete.html', {'restaurant': restaurant})

# def template_loader(request, context, load_template):
# #    try:
#         context['segment'] = load_template
#         print ("Loading... " + load_template)

#         html_template = loader.get_template(load_template)
#         return HttpResponse(html_template.render(context, request))
