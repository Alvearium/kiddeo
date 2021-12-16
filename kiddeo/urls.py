from django.urls import path
from django.conf import settings
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.static import static
from blog.views import blogView, postView
from restaurants.views import foodsView, foodView
from premises.views import premisesView, premiseView
from photos.views import photosView, serviceView
from holidays.views import holidaysView, holidayView
from animators.views import animatorsView, animatorView
from decorations.views import decorationsView, decorationView
from mainapp.views import indexView, AddComment, AddProductView, ConciergeServiceView,  cartView, quizView, quizResultView, checkoutView, MiniProductsCategoryFilter, SidebarFilters, AddCart, OutputModalData, DeleteCart
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name = 'index'),
    path('cart/', cartView, name = 'cart'),
    path('quiz/', quizView, name = 'quiz'),
    path('quiz/result/', quizResultView, name = 'quiz_result'),
    path('checkout/', checkoutView, name = 'checkout'),
    path('blog/', blogView, name = 'blog'),
    path('categories/foods/', foodsView, name = 'foods'),
    path('categories/photos/', photosView, name = 'photos'),
    path('categories/holidays/', holidaysView, name = 'holidays'),
    path('categories/premises/', premisesView, name = 'premises'),
    path('categories/animators/', animatorsView, name = 'animators'),
    path('add-product/', AddProductView, name = 'add-product'),
    path('blog/post/<slug:post_slug>/', postView, name = 'post'),
    path('product/food/<slug:food_slug>', foodView, name = 'foodProduct'),
    path('categories/decorations/', decorationsView, name = 'decorations'),
    path('concierge-service/', ConciergeServiceView, name = 'concierge_service'),
    path('product/service/<slug:service_slug>/', serviceView, name = 'serviceView'),
    path('product/premise/<slug:premise_slug>/', premiseView, name = 'premiseProduct'),
    path('product/holiday/<slug:holiday_slug>/', holidayView, name = 'holidayProduct'),
    path('product/animator/<slug:animator_slug>/', animatorView, name = 'animatorProduct'),
    path('product/decoration/<slug:decoration_slug>', decorationView, name = 'decorationProduct'),
    path('ajax/add-cart/', AddCart, name = 'AddCart'),
    path('ajax/add-blog-comment/', AddComment, name = 'AddComment'),
    path('ajax/delete-cart/', DeleteCart, name = 'DeleteCart'),
    # path('ajax/load-more-tabs/', LoadMoreTabs, name = 'LoadMoreTabs'),
    path('ajax/data-output-to-modal/', OutputModalData, name = 'OutputModalData'),
    path('ajax/sidebar-filters/', SidebarFilters, name = 'SidebarFilters'),
    path('ajax/mini-products-category-filter/', MiniProductsCategoryFilter, name = 'MiniProductsCategoryFilter'),
    url(r'mdeditor/', include('mdeditor.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)