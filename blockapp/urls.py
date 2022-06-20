from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    # url path to add business, post,neighbourhood forms
    path('<str:username>/add/business/', views.AddBusiness, name='AddBusiness'),
    path('<str:username>/add/neighbourhood/', views.AddNeighbourhood, name='AddNeighbourhood'),
    path('<str:username>/add/post/', views.new_post, name='AddPost'),

   
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)