from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import *

urlpatterns = [
    path('',views.home, name='home'),
    # url path to add business, post,neighbourhood forms
    path('add/business/', views.AddBusiness, name='AddBusiness'),
    path('add/neighbourhood/', views.AddNeighbourhood, name='AddNeighbourhood'),
    path('add/post/', views.new_post, name='AddPost'),
    # path to form output
    path('neighbourhoods/', views.MyNeighbourhoods, name='MyNeighbourhoods'),
    path('posts/', views.MyPosts, name='MyPosts'),
    path('businesses/', views.MyBusinesses, name='MyBusinesses'),
    # search business path
    path('search', views.Search, name="Search"),
    # path to view individual neighbourhoods
    path('neighbourhood/<str:title>/', views.SingleNeighbourhood, name='SingleNeighbourhood'),


   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)