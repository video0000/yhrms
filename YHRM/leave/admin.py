# -*-coding:utf-8 -*-
from django.contrib import admin
from django_admin_bootstrapped.admin.models import CollapsibleInline
from import_export import resources
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin

from .models import *


# Register your models here.
class LeaveResource(resources.ModelResource):
    class Meta:
        model = Leave


@admin.register(Leave)
class LeaveAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee', 'name', 'leave_type', 'start_date', 'end_date', 'duration', 'reason')
    search_fields = ['employee__name', ]
    resource_class = LeaveResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'


class Exchanging_HolidayInline(admin.StackedInline, CollapsibleInline, ):
    model = Exchanging_Holiday
    extra = 0


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'start_date', 'end_date',)
    search_fields = ['name', ]
    inlines = [Exchanging_HolidayInline, ]
    resource_class = LeaveResource


@admin.register(Exchanging_Holiday)
class Exchange_HolidayAdmin(admin.ModelAdmin):
    list_display = ('holiday', 'date')

