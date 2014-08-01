from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dongtaoy_oa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # assets urls
    url(r'^asset/', include('administration.asset.urls')),

    # assets category urls
    url(r'^category/', include('administration.category.urls'))
)
