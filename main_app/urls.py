from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.main, name='main'),
    path('profile', views.profile, name='profile')
]