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
    url(r'^searchscript/(?P<scriptstring>.+)/', 'osfw.views.searchscript'),
    url(r'^searchlicense/(?P<licensestring>.+)/', 'osfw.views.searchlicense'),

    url(r'^get/(?P<osfw_id>\d+)/', 'osfw.views.fontinfo'),
    url(r'^like/(?P<osfw_id>\d+)/', 'osfw.views.likefont'),


    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^accounts/login/', 'openshift.views.login'),
#    url(r'^accounts/auth/', 'openshift.views.auth_view'),
#    url(r'^accounts/logout/', 'openshift.views.logout'),
#    url(r'^accounts/loggedin/', 'openshift.views.loggedin'),
#    url(r'^accounts/invalid/', 'openshift.views.invalid_login'),
#    url(r'^accounts/register/', 'openshift.views.register_user'),
#    url(r'^accounts/register_success/', 'openshift.views.register_success'),

    #url from django-registration
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', 'openshift.views.loggedin'),
#   openid
#    url(r'^$', 'openshift.app.views.home'),
    url(r'^signup-email/', 'openshift.views.signup_email'),
    url(r'^email-sent/', 'openshift.views.validation_sent'),
    url(r'^login/$', 'openshift.views.home'),
    url(r'^done/$', 'openshift.views.done', name='done'),
    url(r'^email/$', 'openshift.views.require_email', name='require_email'),

    url('', include('social.apps.django_app.urls', namespace='social'))

)

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

