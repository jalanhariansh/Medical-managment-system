from django.urls import path,include
from . import views
from django.contrib.auth import get_user_model
from .views import (
    PostCreateView,
)

urlpatterns = [
    path('',views.basic,name='patient-home'),
    path('<str:username>',views.home,name='patient-profile'),
    path('book/',PostCreateView.as_view(),name='patient-book'),
    path('accounts/', views.accounts,name='patient-accounts'),
    path('chat/<str:room_name>/', views.chats,name='patient-chat'),
    path('chat/', views.chathome,name='patient-chat-home'),
]