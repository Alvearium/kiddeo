from django.contrib import admin
from django.urls import path
from mainapp.views import indexView, cartView
from animators.views import animatorsView, animatorView
from decorations.views import decorationsView, decorationView
from premises.views import premisesView, premiseView
from restaurants.views import foodsView, foodView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name = 'index'),
    path('categories/animators/', animatorsView, name = 'animators'),
    path('product/animator/', animatorView, name = 'animatorProduct'),
    path('categories/decorations/', decorationsView, name = 'decorations'),
    path('product/decoration/', decorationView, name = 'decorationProduct'),
    path('categories/premises/', premisesView, name = 'premises'),
    path('product/premise/', premiseView, name = 'premiseProduct'),
    path('categories/foods/', foodsView, name = 'foods'),
    path('product/food/', foodView, name = 'foodProduct'),
    path('cart/', cartView, name = 'cart'),
    
]
