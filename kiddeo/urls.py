from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from restaurants.views import foodsView, foodView
from premises.views import premisesView, premiseView
from animators.views import animatorsView, animatorView
from decorations.views import decorationsView, decorationView
from mainapp.views import indexView, cartView, MiniProductsCategoryFilter, SidebarFilters

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name = 'index'),
    path('cart/', cartView, name = 'cart'),
    path('categories/foods/', foodsView, name = 'foods'),
    path('categories/premises/', premisesView, name = 'premises'),
    path('categories/animators/', animatorsView, name = 'animators'),
    path('categories/decorations/', decorationsView, name = 'decorations'),
    path('product/food/<slug:food_slug>', foodView, name = 'foodProduct'),
    path('product/premise/<slug:premise_slug>/', premiseView, name = 'premiseProduct'),
    path('product/animator/<slug:animator_slug>/', animatorView, name = 'animatorProduct'),
    path('product/decoration/<slug:decoration_slug>', decorationView, name = 'decorationProduct'),
    path('ajax/sidebar-filters/', SidebarFilters, name = 'SidebarFilters'),
    path('ajax/mini-products-category-filter/', MiniProductsCategoryFilter, name = 'MiniProductsCategoryFilter'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)