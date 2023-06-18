from django.urls import reverse
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout


class RestrictUserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.find("/staff/") > -1:  # restricted admin url for custom admin site
           if not request.user.is_staff:
              logout(request)
              messages.warning(request,'Please login as a staff')
              return redirect(reverse('login'))
        response = self.get_response(request)
        return response