"""department URL Configuration

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
from django.conf.urls import url

from . import views as dp_views

urlpatterns = [

    url(r'^list/', dp_views.department_list, name='DEPARTMENT_LIST'),
    url(r'^detail/(?P<department_number>\w+)$', dp_views.department_detail, name='DEPARTMENT_DETAIL'),
    url(r'^detail/(?P<department_number>\w+)/delete$', dp_views.department_delete, name='DEPARTMENT_DELETE'),
    url(r'^detail/(?P<department_number>\w+)/change$', dp_views.department_change, name='DEPARTMENT_CHANGE'),
]
