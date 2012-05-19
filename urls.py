from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'congresvoorstel.views.home', name='home'),
    # url(r'^congresvoorstel/', include('congresvoorstel.foo.urls')),

    url(r'^amendement/$', 'congresvoorstel.voorstel.views.new_amendement'),
    url(r'^amendement/(?P<slug>[a-zA-Z0-9]{32})/$',
        'congresvoorstel.voorstel.views.amendement'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
