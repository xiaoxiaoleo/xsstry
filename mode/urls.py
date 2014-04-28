from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'mode.views.index', name = 'mode_index'),
	url(r'^(?P<mode_id>\d+)/$', 'mode.views.detail', name = 'mode_detail'),
)