from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^interesting$', views.interesting, name='interesting'),
    url(r'^trash$', views.trash, name='trash'),
    url(r'^settings$', views.settings, name='settings'),
]
