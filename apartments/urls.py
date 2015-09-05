from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.new, name='new'),
    url(r'^$', views.interesting, name='interesting'),
    url(r'^$', views.trash, name='trash'),
    url(r'^$', views.settings, name='settings'),
]
