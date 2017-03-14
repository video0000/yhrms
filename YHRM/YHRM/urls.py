"""YHRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from YHRM import settings
from base_site import views as bs_views
from department import urls as dp_urls
from employee import urls as ey_urls
from leave import urls as le_urls

urlpatterns = [
    # base_site
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', bs_views.index, name='BP_INDEX'),
    url(r'^accounts/change/profile$', bs_views.change_my_profile, name='BP_CHANGE_MY_PROFILE'),
    url(r'^accounts/change/avatar', bs_views.change_my_avatar, name='BP_CHANGE_MY_AVATAR'),
    url(r'^accounts/change/password$', bs_views.change_my_password, name='BP_CHANGE_MY_PASSWORD'),
    url(r'^accounts/detail/profile$', bs_views.my_profile, name='BP_MYPROFILE'),
    url(r'^login$', bs_views.login, name='BP_LOGIN'),
    url(r'^logout$', bs_views.logout, name='BP_LOGOUT'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # department
    url(r'^department/', include(dp_urls, namespace='DEPARTMENT')),
    # employee
    url(r'^employee/', include(ey_urls, namespace='EMPLOYEE')),
    # leave
    url(r'^leave/', include(le_urls, namespace='LEAVE')),
    url(r'^report/', include('report_builder.urls')),
    url(r'^explorer/', include('explorer.urls')),
]
