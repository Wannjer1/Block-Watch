from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # url path to add business, post,neighbourhood forms
    path('add/business/', views.AddBusiness, name='AddBusiness'),
    path('/add/neighbourhood/', views.AddNeighbourhood, name='AddNeighbourhood'),
    path('/add/post/', views.new_post, name='AddPost'),

   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)