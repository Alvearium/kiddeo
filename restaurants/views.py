import json
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Avg, Max, Min
from django.shortcuts import get_object_or_404
from mainapp.views import addPurchasesViewed, productRecommendation
from restaurants.models import Restaurant, Food, ImageLibrary, Reviews, Questions, Audits, AuditElement

# Create your views here.
def foodsView(request):
    restaurants = Restaurant.objects.all()[:7]
    restaurants_count = Restaurant.objects.all().count()
    
    for restaurant in restaurants:
        restaurant.additional_data = Food.objects.filter(restaurant=restaurant)[:4]
        
    return render(request, 'foods.html', {"restaurants": restaurants, "restaurants_count": restaurants_count})

def foodView(request, food_slug):
    subcategories = []
    restaurant = get_object_or_404(Restaurant, slug=food_slug)
    foods = Food.objects.filter(restaurant=restaurant)
    audit = Audits.objects.filter(agency_id=restaurant.id)[:2]
    reviews = Reviews.objects.filter(restaurant_id=restaurant.id)[:2]
    questions = Questions.objects.filter(restaurant_id=restaurant.id)[:2]
    recommendations = productRecommendation()

    if not request.session.get('viewed_products'):
        request.session['viewed_products'] = list()
        listPurchasesViewed = False
    else:
       listPurchasesViewed = request.session['viewed_products']    
    
    for food in foods:
        if not food.subcategory in subcategories:
            subcategories.append(food.subcategory)

    if not audit:
        audit_elements = False
    else:
        audit_elements = AuditElement.objects.filter(audit_id=audit[0].id)[:2]

    if not questions:
        questions = False

    if not reviews:
        reviews = False
        
    if not listPurchasesViewed: 
        listPurchasesViewed = False
        
    return render(request, 'food.html', {
        'restaurant': restaurant,
        'foods': foods,
        'name': 'food',
        'subcategories': subcategories,
        'audit_elements': audit_elements,
        'reviews': reviews,
        'questions': questions,
        'recommendations': recommendations,
        'listPurchasesViewed': listPurchasesViewed
    })