from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gacha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'gacha.views.home', name='home'),
    url(r'^games/', include('games.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
