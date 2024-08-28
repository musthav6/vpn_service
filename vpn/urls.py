from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='vpn/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='vpn/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('sites/', views.user_sites, name='sites'),
    path('sites/add/', views.add_site, name='add_site'),
    path('sites/<int:site_id>/', views.proxy, name='proxy'),
    path('statistics/', views.statistics, name='statistics'),
]
