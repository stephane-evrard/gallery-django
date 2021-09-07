from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('search/', search_images, name='search_results'),
    path('image/<int:id>', get_image, name='image_results'),
    path('location/<str:location>/', location, name='location_results'),
    path('category/<str:category>', category, name='category_results'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)