from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_page import views
from main_page.views import MainViewSet



urlpatterns = [
    path('', views.main_page, name='home'),
    path('about_restaurant/', views.about_restaurant, name='about_restaurant'),
]