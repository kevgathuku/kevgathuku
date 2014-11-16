from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import IndexView, category

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kevgathuku.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',IndexView.as_view(), name='home'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^about-this-site/$', 'blog.views.about_site', name='about_site'),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    url(r'^post/', include('blog.urls', namespace='blog')),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', category, name='category'),
)
