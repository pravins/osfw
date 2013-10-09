from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'osfw.views.redirect_to_index'),
    url(r'^index/$', 'osfw.views.index'),
    url(r'^about/$', 'osfw.views.about'),
    url(r'^peoples/$', 'osfw.views.peoples'),
    url(r'^standards/$', 'osfw.views.standards'),
    url(r'^index/allfonts/$', 'osfw.views.allfonts'),
    url(r'^index/fontinfo/$', 'osfw.views.fontinfo'),
#    url(r'^index/searchfonts/$', 'osfw.views.search_fonts'),
    url(r'^index/search/$', 'osfw.views.search'),
    url(r'^index/test/$', 'osfw.views.test'),

    url(r'^get/(?P<osfw_id>\d+)/', 'osfw.views.fontinfo'),
    url(r'^like/(?P<osfw_id>\d+)/', 'osfw.views.likefont'),

#    url(r'^osfw/$', include('osfw.urls')),
    # url(r'^$', 'myprj.views.home', name='home'),
    # url(r'^myprj/', include('myprj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
