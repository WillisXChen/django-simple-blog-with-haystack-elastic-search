from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'haystack_example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^blog/', include('simpleblog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

