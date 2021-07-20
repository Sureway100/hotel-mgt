from django.urls import path
from . import views


# first arg means home, second arg means function that is returned, inside views select home, then name path
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
]
