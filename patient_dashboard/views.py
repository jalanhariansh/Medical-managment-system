from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Appointment
from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.views.generic import (
    CreateView,
)
from django.db.models import Sum
from django.db.models import Q
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
# Create your views here.

def home(request):
   user = request.user
   if request.method=='POST':
      u_form = UserUpdateForm(request.POST, instance=user)
      p_form = ProfileUpdateForm(request.POST, instance=request.user.patient)
      if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)("apps", {'type': 'chatroom_message','message': 'refresh_profiles',})
            messages.success(request, f'your account has been updated')
   else:
      u_form = UserUpdateForm(instance=user)
      p_form = ProfileUpdateForm(instance=request.user.patient)
   apps = Appointment.objects.filter(patient = user).order_by('-date_posted')
   return render(request,'patient_dashboard/profile.html',{'user': user, 'apps': apps, 'u_form' : u_form, 'p_form' : p_form})

def accounts(request):
   apps = Appointment.objects.filter(patient = request.user)
   total_price = apps.aggregate(Sum('cost'))['cost__sum']
   return render(request,'patient_dashboard/accounts.html',{'apps': apps, 'total_price': total_price})

class PostCreateView(CreateView):
    model = Appointment
    fields = ["doc_name", "department", "symptoms"]

    def form_valid(self,form):
        form.instance.patient = self.request.user
        final = super().form_valid(form)
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)("apps", {'type': 'chatroom_message','message': 'refresh_apps',})
        return final
    
def chats(request,room_name):
   users = get_user_model()
   user = get_object_or_404(users, username=room_name[len(request.user.username):])
   search = ''
   if 'q' in request.GET:
      q = request.GET['q']
        # data = Data.objects.filter(last_name__icontains=q)
      multiple_q = Q((Q(first_name__icontains=q) | Q(last_name__icontains=q)) & Q(is_staff=True))
      data = users.objects.filter(multiple_q)
      search = q
   else:
      data = users.objects.filter(is_staff=True)
   return render(request,'patient_dashboard/chats.html',{'view_user': user,'all_users': data,'room_name': room_name,'cur_user': request.user, 'search': search})

def chathome(request):
   users = get_user_model()
   return HttpResponseRedirect('/patient/chat/'+request.user.username+users.objects.filter(is_staff=True).first().username)