from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^interesting$', views.interesting, name='interesting'),
    url(r'^trash$', views.trash, name='trash'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^api/post$', views.update_post, name='post'),
    url(r'^api/post/(?P<post_id>[0-9_]+)$', views.update_post, name='post')
]
