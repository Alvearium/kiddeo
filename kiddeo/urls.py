from django.contrib import admin
from django.urls import path
from mainapp.views import indexView
from animators.views import animatorsView
from decorations.views import decorationsView
from premises.views import premisesView
from restaurants.views import foodsView

urlpatterns = [
    path('', indexView, name = 'index'),
    path('categories/animators/', animatorsView, name = 'animators'),
    path('categories/decorations/', decorationsView, name = 'decorations'),
    path('categories/premises/', premisesView, name = 'premises'),
    path('categories/foods/', foodsView, name = 'foods'),
    path('admin/', admin.site.urls),
]
