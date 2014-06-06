from django.conf.urls import patterns, include, url
from mysite.views import search_form,search,api_creation,updateCache
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', search_form),
    url(r'^search/$',search),
    url(r'^api/$',api_creation),
    url(r'^update/$',updateCache),
)
