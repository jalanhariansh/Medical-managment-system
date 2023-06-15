from django.urls import path,include
from . import views
from .forms import AppUpdateForm
from .views import AppListView

urlpatterns = [
    path('',AppListView.as_view(),name='staff-home'),
    path('profiles/',views.basic,name='staff-profile-home'),
    path('profiles/<str:username>', views.profiles, name='staff-profiles'),
    path('apps/<int:pk>/', AppUpdateForm.as_view(template_name="staff_dashboard/appointment_form.html"), name='staff-apps'),
    path('chat/<str:room_name>/', views.chats,name='staff-chat'),
    path('chat/', views.chathome,name='staff-chat-home'),
]