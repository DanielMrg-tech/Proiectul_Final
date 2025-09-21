from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main_page import views
from main_page.views import MainViewSet


router = DefaultRouter()
router.register('menus', MainViewSet, basename='meniu_viewset')


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about_restaurant/', views.about_restaurant, name='about_restaurant'),
    path('api/', include(router.urls)),

    path('meniu/', views.meniu_view, name='meniu'),
    path('meniu/<int:pk>/delete/', views.delete_meniu, name='delete_meniu'),
    path('meniu/<int:pk>/edit/', views.update_meniu, name='update_meniu'),
    path('users/<int:user_id>/meniu/', views.meniu_by_user, name='meniu_by_user')
]