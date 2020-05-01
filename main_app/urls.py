from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('listings/', views.list, name='list'),
    path('messages/', views.messages, name='messages'),
    path('new-listing/', views.new_list, name='new-listing'),
    path('profile/', views.profile, name='profile')
]
