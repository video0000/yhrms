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

from . import views as ey_views

urlpatterns = [

    url(r'^list/', ey_views.employee_list, name='EMPLOYEE_LIST'),
    url(r'^transfer/list/', ey_views.transfer_order_list, name='TRANSFER_LIST'),
    url(r'^transfer/detail/(\w+)', ey_views.transfer_order_detail, name='TRANSFER_DETAIL'),
    url(r'^transfer/change/(\w+)', ey_views.transfer_order_change, name='TRANSFER_DETAIL_CHANGE'),
    url(r'^transfer/doc/(\w+)', ey_views.transfer_order_doc, name='TRANSFER_ORDER_DOC'),
    url(r'^transfer/add/(\w+)', ey_views.transfer_order_add, name='TRANSFER_ORDER_ADD'),
    url(r'^transfer/synchro/(\w+)', ey_views.transfer_order_synchro, name='TRANSFER_ORDER_SYNCHRO'),
    url(r'^transfer/synchroback/(\w+)', ey_views.transfer_order_synchro_back, name='TRANSFER_ORDER_SYNCHRO_BACK'),
    url(r'^transfer/delete/(\w+)', ey_views.transfer_order_delete, name='TRANSFER_ORDER_DELETE'),
    url(r'^detail/(?P<employee_number>\w+)/(?P<content_type>\w+)$', ey_views.employee_detail, name='EMPLOYEE_DETAIL'),
    url(r'^resume/(?P<employee_number>\w+)/$', ey_views.employee_resume, name='EMPLOYEE_RESUME'),
    # url(r'^detail/(?P<department_number>\w+)/delete$', dp_views.department_delete, name='DEPARTMENT_DELETE'),
    url(r'^delete_confirm/(\w+)/(\w+)/(\w+)$', ey_views.employee_content_delete_confirm, name='EMPLOYEE_DELETE_CONFIRM'),
    url(r'^delete/(\w+)/(\w+)/(\w+)$', ey_views.employee_content_delete, name='EMPLOYEE_DELETE'),
    url(r'^change/(\w+)/(\w+)/(\w+)$', ey_views.employee_content_change, name='EMPLOYEE_CHANGE'),
    url(r'^content/add/(\w+)/(\w+)/(\w+)$', ey_views.employee_detail_add, name='EMPLOYEE_CONTENT_ADD'),

    url(r'^dimission/list', ey_views.dimission_list, name='DIMISSION_LIST'),
    url(r'^dimission/add/(\w+)', ey_views.dimission_add, name='DIMISSION_ADD'),
    url(r'^dimission/delete/(\w+)', ey_views.dimission_delete, name='DIMISSION_DELETE'),

]