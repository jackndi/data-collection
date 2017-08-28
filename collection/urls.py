from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^brand/$', views.BrandList.as_view(), name='brand-list'),
    url(r'^brand/(?P<pk>[0-9]+)$', views.BrandDetail.as_view(), name='brand-detail'),
    url(r'^person/$', views.PersonList.as_view(), name='person-list'),
    url(r'^person/(?P<pk>[0-9]+)$', views.PersonDetail.as_view(), name='person-detail'),
    url(r'^location/$', views.LocationList.as_view(), name='location-list'),
    url(r'^location/(?P<pk>[0-9]+)$', views.LocationDetail.as_view(), name='location-detail'),
    url(r'^data/$', views.DataList.as_view(), name='data-list'),
    url(r'^data/(?P<pk>[0-9]+)$', views.DataDetail.as_view(), name='data-detail'),
    url(r'^user/(?P<pk>[0-9]+)$', views.UserView.as_view(), name='user-detail'),
]