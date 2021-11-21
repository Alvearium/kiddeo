import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg, Max, Min
from django.shortcuts import get_object_or_404
from restaurants.models import Restaurant, Food

# Create your views here.
def foodsView(request):
    restaurants = Restaurant.objects.all()[:20]
    restaurants_count = Restaurant.objects.all().count()
    return render(request, 'foods.html', {"restaurants": restaurants, "restaurants_count": restaurants_count})

def foodView(request, food_slug):
    subcategories = []
    restaurant = get_object_or_404(Restaurant, slug=food_slug)
    foods = Food.objects.filter(restaurant=restaurant)
    for food in foods:
        if not food.subcategory in subcategories:
            subcategories.append(food.subcategory)
    return render(request, 'food.html', {
        "restaurant": restaurant,
        "foods": foods,
        "name": "food",
        "subcategories": subcategories
    })