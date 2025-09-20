from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]

if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)