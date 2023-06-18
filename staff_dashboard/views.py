from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from patient_dashboard.models import Appointment
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import AppUpdateForm
from django.views.generic import ListView
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


# Create your views here.
#def home(request):
#    apps = Appointment.objects.all()
#    return render(request,'staff_dashboard/home.html',{'apps': apps})

class AppListView(ListView):
    model = Appointment
    template_name = 'staff_dashboard/home.html'
    context_object_name = "apps"
    ordering = ['-date_posted']

def profiles(request, username):
   users = get_user_model().objects.filter(is_patient=True)
   user = get_object_or_404(users, username=username)
   apps = Appointment.objects.filter(patient = user).order_by('-date_posted')
   return render(request,'staff_dashboard/profile.html',{'view_user': user,'all_users': users,'apps': apps})

def basic(request):
   return HttpResponseRedirect('/staff/profiles/'+get_user_model().objects.filter(is_patient=True).first().username)

def chats(request,room_name):
   users = get_user_model()
   print(room_name[:-len(request.user.username)])
   user = get_object_or_404(users, username=room_name[:-len(request.user.username)])
   return render(request,'staff_dashboard/chats.html',{'view_user': user,'all_users': users.objects.filter(is_patient=True),'room_name': room_name,'cur_user': request.user})

def chathome(request):
   users = get_user_model()
   return HttpResponseRedirect('/staff/chat/'+users.objects.filter(is_patient=True).first().username+request.user.username)

def approve(request,pk):
    app = Appointment.objects.get(id=pk)
    if request.method=='POST':
        form = AppUpdateForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
            form.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("apps", {'type': 'chatroom_message','message': 'refresh_apps',})
            messages.success(request, f'prescription has been uploaded')
            return redirect('staff-home')
    else:
        form = AppUpdateForm(instance=Appointment.objects.get(id=pk))
    context = {
        'form' : form,
        'app' : app,
    }
    return render(request,'staff_dashboard/appointment_form.html',context)