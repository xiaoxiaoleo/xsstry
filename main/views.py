from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

from django.contrib.auth.decorators import login_required

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.

def login(request):
  if(request.method == 'GET'):
    return render(request, 'main/login.html', {'error': False,})
  else:
    username = request.POST.get('user', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)
    if user is not None and user.is_active:
      auth.login(request, user)
      return HttpResponseRedirect(reverse('main:index'))
    else:
      return render(request, 'main/login.html', {'error': True,})

def register(request):
  if(request.method == 'GET'):
    return render(request, 'main/register.html', {'error': False,})

@login_required
def index(request):
  return render(request, 'main/index.html')

@login_required
def logout(request):
  auth.logout(request)
  return HttpResponseRedirect(reverse('main:login'))
