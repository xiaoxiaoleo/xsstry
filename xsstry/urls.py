from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^proj/', include('proj.urls', namespace = "proj")),
    url(r'^mode/', include('mode.urls', namespace = "mode")),
    url(r'^note/', include('note.urls', namespace = "note")),
    url(r'^seti/', include('seti.urls', namespace = "seti")),
    url(r'^', include('main.urls', namespace = "main")),
)
