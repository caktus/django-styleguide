from django.conf.urls import url, patterns
from . import views


urlpatterns = patterns('',
    url(r'^$',
        views.styleguide,
        name='styleguide'),
    url(r'^(?P<name>[0-9A-Za-z_\-]+)/$', views.styleguide_page, name="styleguide_page"),
)
