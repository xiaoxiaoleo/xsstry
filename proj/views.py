from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from proj.models import XssProject, XssItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth

# Create your views here.
@login_required
def index(request):
    project_list = request.user.xssproject_set.order_by('-create_date')
    return render(request, 'proj/index.html', {'error': False, 'project_list': project_list})

@login_required
def detail(request, proj_id):
    project_list = request.user.xssproject_set.order_by('-create_date')
    selected_project = get_object_or_404(XssProject, owner = request.user, pk = proj_id)
    item_list = selected_project.xssitem_set.order_by('-recv_date')
    return render(
        request, 
        'proj/detail.html', 
        {
            'error': False, 
            'project_list': project_list, 
            'proj_id': proj_id, 
            'item_list': item_list 
        }
    )
