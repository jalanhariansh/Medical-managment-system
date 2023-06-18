from django.urls import path,include
from . import views
from .views import AppListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',AppListView.as_view(),name='staff-home'),
    path('profiles/',views.basic,name='staff-profile-home'),
    path('profiles/<str:username>', views.profiles, name='staff-profiles'),
    path('apps/<int:pk>/', views.approve, name='staff-apps'),
    path('chat/<str:room_name>/', views.chats,name='staff-chat'),
    path('chat/', views.chathome,name='staff-chat-home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)