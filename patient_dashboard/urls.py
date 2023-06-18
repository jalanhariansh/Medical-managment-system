from django.urls import path,include
from . import views
from django.contrib.auth import get_user_model
from .views import (
    PostCreateView,
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='patient-home'),
    path('book/',PostCreateView.as_view(),name='patient-book'),
    path('accounts/', views.accounts,name='patient-accounts'),
    path('chat/<str:room_name>/', views.chats,name='patient-chat'),
    path('chat/', views.chathome,name='patient-chat-home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)