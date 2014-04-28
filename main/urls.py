from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^$', 'main.views.index', name = 'index'),
    url(r'^login/$', 'main.views.login', name = 'login'),
    url(r'^register/$', 'main.views.register', name = 'register'),

)
