# -*-coding:utf-8-*-
from django.contrib import admin
from django_admin_bootstrapped.admin.models import CollapsibleInline
from .models import *
from simple_history.admin import SimpleHistoryAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class TransferOrderResource(resources.ModelResource):
    class Meta:
        model = TransferOrder


@admin.register(TransferOrder)
class TransferOrderAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ('transfer_number', 'name', 'old_department', 'old_job', 'new_department', 'new_job', 'transfer_date',
                    'new_department_salary_calculate_start_date','confirm')
    list_filter = ('employee__department',)
    search_fields = ['employee_name', ]
    resource_class = TransferOrderResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'

    # def old_deparment(self, obj):
    #     return u'%s' % obj.employee.department.name
    #
    # old_deparment.short_description = u'原部门'
    #
    # def old_job(self, obj):
    #     return u'%s' % obj.employee.job
    #
    # old_job.short_description = u'原岗位'


class ContractInline(admin.StackedInline, CollapsibleInline, ):
    model = Contract
    extra = 0


class ContractResource(resources.ModelResource):
    class Meta:
        model = Contract


@admin.register(Contract)
class ContractAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = ('employee', 'name', 'start_date', 'end_date', 'duration')
    list_filter = ('employee__department',)
    search_fields = ['employee__name', ]
    resource_class = ContractResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'


class EductionInline(admin.StackedInline, CollapsibleInline, ):
    model = Eduction
    extra = 0


class EductionResource(resources.ModelResource):
    class Meta:
        model = Eduction


@admin.register(Eduction)
class EductionAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee', 'name', 'start_date', 'end_date', 'qualification', 'degree', 'major', 'graduate_from', 'type')
    list_filter = ('employee__department',)
    search_fields = ['employee__name', ]
    resource_class = EductionResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'


class WorkExperienceInline(admin.StackedInline, CollapsibleInline, ):
    model = WorkExperience
    extra = 0


class WorkExperienceResource(resources.ModelResource):
    class Meta:
        model = WorkExperience


@admin.register(WorkExperience)
class WorkExperienceAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee', 'name', 'start_date', 'end_date', 'department', 'job',)
    list_filter = ('employee__department',)
    search_fields = ['employee__name', ]
    resource_class = EductionResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'


class RelationShipInline(admin.StackedInline, CollapsibleInline, ):
    model = RelationShip
    extra = 0


class RelationShipResource(resources.ModelResource):
    class Meta:
        model = RelationShip


@admin.register(RelationShip)
class RelationShipAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee', 'name', 'relation', 'birthday', 'political_status', 'graduate_from', 'job')
    list_filter = ('employee__department',)
    search_fields = ['employee__name', ]
    resource_class = RelationShipResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'


class RemarkInline(admin.StackedInline, CollapsibleInline, ):
    model = Remark
    extra = 0


class RemarkResource(resources.ModelResource):
    class Meta:
        model = Remark


@admin.register(Remark)
class RemarkAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee', 'name', 'remark',)
    list_filter = ('employee__department',)
    search_fields = ['employee__name', ]
    resource_class = RemarkResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Employee
        import_id_fields = ('employee_number',)


@admin.register(Employee)
class EmployeeAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee_number','name', 'first_eduction', 'avatar_preview', 'gender', 'nationality', 'age',
        'work_age', 'local_age', 'employee_type',
        'titles', 'department', 'department_type', 'job', 'political_status',
        'identification_card', 'home_address')
    list_filter = ('department',)
    search_fields = ['name','employee_number' ]
    raw_id_fields = ['department', ]

    def department_type(self, obj):
        try:
            department_type = obj.department.get_type_display()
        except:
            department_type = ""
        return department_type

    department_type.short_description = u'部门类别'

    # def contract_start_date(self, obj):
    #     try:
    #         start_date=obj.contracts.start_date
    #     except:
    #         start_date=u'无合同开始日期'
    #     return start_date
    #
    # contract_start_date.short_description = u'合同开始日期'
    #
    # def contract_end_date(self, obj):
    #     try:
    #         end_date = obj.contracts.end_date
    #     except:
    #         end_date = u'无合同结束日期'
    #     return end_date
    #
    # contract_end_date.short_description = u'合同结束日期'
    #
    # def contract_duration(self, obj):
    #     return obj.contracts.get_duration_display()
    #
    # contract_duration.short_description = u'合同期限'

    def first_eduction(self, obj):
        try:
            first_eduction = obj.eductions.filter(type='first')[0]
        except:
            first_eduction = u'没有第一学历信息'
        return first_eduction

    first_eduction.short_description = u'第一学历'

    resource_class = EmployeeResource
    inlines = [ContractInline, EductionInline, WorkExperienceInline, RelationShipInline, RemarkInline]

class DimissionResource(resources.ModelResource):
    class Meta:
        model = Dimission


@admin.register(Dimission)
class DimissionAdmin(SimpleHistoryAdmin, ImportExportModelAdmin):
    list_display = (
        'employee', 'name','dimission_date', 'record_date','reason')
    search_fields = ['employee__name', ]
    resource_class = DimissionResource
    raw_id_fields = ['employee']

    def name(self, obj):
        return u'%s' % obj.employee.name

    name.short_description = u'员工姓名'