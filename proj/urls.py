from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'proj.views.index', name = 'proj_index'),
    url(r'^(?P<proj_id>\d+)/$', 'proj.views.detail', name = 'proj_detail'),

)
