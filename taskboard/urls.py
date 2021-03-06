from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include('taskboard.apps.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
