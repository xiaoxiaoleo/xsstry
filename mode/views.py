from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

from mode.models import XssModel

@login_required
def index(request):
	model_list = request.user.xssmodel_set.all()
	return render(request, 'mode/index.html', {'error': False, 'model_list': model_list})

@login_required
def detail(request, mode_id):
	model_list = request.user.xssmodel_set.all()
  	selected_model = get_object_or_404(XssModel, owner = request.user, pk = mode_id)
  	return render(
  		request, 
  		'mode/detail.html', 
  		{
  			'error': False, 
  			'model_list': model_list, 
  			'selected_model': selected_model, 
  		}
  	)