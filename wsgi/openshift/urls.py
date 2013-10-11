from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'openshift.views.home', name='home'),
#    url(r'^$', 'osfw.views.redirect_to_index'),
    url(r'^$', 'osfw.views.index'),
    url(r'^test/$', 'osfw.views.test'),
    url(r'^about/$', 'osfw.views.about'),
    url(r'^standards/$', 'osfw.views.standards'),
    url(r'^peoples/$', 'osfw.views.peoples'),
    url(r'^contact/$', 'osfw.views.contact'),
    url(r'^allfonts/$', 'osfw.views.allfonts'),
    url(r'^search/$', 'osfw.views.search'),
    url(r'^searchlang/(?P<langstring>.+)/', 'osfw.views.searchlang'),
    url(r'^get/(?P<osfw_id>\d+)/', 'osfw.views.fontinfo'),
    url(r'^like/(?P<osfw_id>\d+)/', 'osfw.views.likefont'),


    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
