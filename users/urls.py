from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('accounts/', include("allauth.urls")), #most important
   path('register/', views.register, name='register'),
   path('login/', views.CustomLogin,name='login'),
   path('logout/', auth_views.LogoutView.as_view(template_name='users/home.html'),name='logout'),
]