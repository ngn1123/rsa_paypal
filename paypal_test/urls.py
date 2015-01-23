from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',

    url(r'^$', views.money_request),
    url(r'^confirm$', views.confirm)
)