from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from .models import Appointment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
)
from django.db.models import Sum
# Create your views here.

def home(request, username):
   users = get_user_model()
   user = get_object_or_404(users, username=username)
   apps = Appointment.objects.filter(patient = user)
   return render(request,'patient_dashboard/profile.html',{'view_user': user,'all_users': users.objects.filter(is_patient=True),'apps': apps})

def basic(request):
   return HttpResponseRedirect('/patient/'+request.user.username)

def accounts(request):
   apps = Appointment.objects.filter(patient = request.user)
   total_price = apps.aggregate(Sum('cost'))['cost__sum']
   return render(request,'patient_dashboard/accounts.html',{'apps': apps, 'total_price': total_price})

class PostCreateView(CreateView):
    model = Appointment
    fields = ["doc_name", "department", "symptoms"]

    def form_valid(self,form):
        form.instance.patient = self.request.user
        return super().form_valid(form)
    
def chats(request,room_name):
   users = get_user_model()
   user = get_object_or_404(users, username=room_name[len(request.user.username):])
   return render(request,'patient_dashboard/chats.html',{'view_user': user,'all_users': users.objects.filter(is_staff=True),'room_name': room_name,'cur_user': request.user})

def chathome(request):
   users = get_user_model()
   return HttpResponseRedirect('/patient/chat/'+request.user.username+users.objects.filter(is_staff=True).first().username)