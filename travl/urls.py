from django.conf.urls import patterns, include, url
import travllist
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'travl.views.home', name='home'),
    # url(r'^travl/', include('travl.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'travllist.views.travelList'),
    url(r'^register', 'travllist.views.register'),
    url(r'^login', 'travllist.views.login'),
    url(r'^travelList', 'travllist.views.travelList'),
    url(r'^logout', 'travllist.views.logout')
)
