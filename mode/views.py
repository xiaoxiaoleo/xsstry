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

@login_required
def create(request):
	if request.method == 'POST':
		model_name = request.POST.get('name')#if not exist return wrong
		if not model_name:
			return render(request, 'mode/new.html', {'error': True})
		m = XssModel.objects.create(
			owner = request.user,
			name = model_name)
		#Todo_list: move to modify.
		m.description = request.POST.get('desc')
		m.set_configparams( config_list = request.POST.getlist('config') )
		m.set_recvparams( param_list = request.POST.getlist('params') )
		request.POST.get('ispublic')
		if request.POST.get('ispublic'):
			m.is_public = True
		else:
			m.is_public = False
		m.save()
		return HttpResponseRedirect(reverse('mode.detail', mode_id = m.id))
	else:
		return render(request, 'mode/new.html', {'error': False})

@login_required
def modify(request, mode_id):



@login_required
def delete(request, mode_id):