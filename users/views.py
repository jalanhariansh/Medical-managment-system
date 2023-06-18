from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def home(request):
    try:
        if request.user.is_patient:
            return redirect(reverse('patient-home'))
        elif request.user.is_staff:
            return redirect(reverse('staff-home'))
        return render(request,'users/home.html')
    except:
        return render(request,'users/home.html')

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'You are successfuly registered')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def CustomLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user:
            if user.is_staff:
                login(request,user)
                return redirect(reverse('staff-home'))
            else:
               messages.warning(request,'Please login as a patient')
               return redirect(reverse('home'))
        else:
            messages.warning(request,'username or password not correct')
            return redirect(reverse('login'))
        
                
    else:
        form = AuthenticationForm()
    return render(request,'users/login.html',{'form':form})