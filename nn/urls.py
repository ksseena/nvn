  
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('simple_upload/',views.simple_upload,name='simple_upload'),
    path('logout',views.logout,name='logout'),
    path('f1',views.f1,name='f1'),
    path('home1',views.home1, name='home1'),
]
