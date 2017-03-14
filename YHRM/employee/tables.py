# -*-coding:utf-8-*-
from tablib.packages.omnijson.core import options

from employee.admin import DimissionAdmin
from table.utils import A

from .models import Employee, TransferOrder, Dimission

from table.columns import Column
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table import Table


class EmployeeList(Table):
    employee_number = Column(field='employee_number', header=u'员工编号')
    name = Column(field='name', header=u'员工姓名')
    id_card = Column(field='identification_card', header=u'身份证号码')
    gender = Column(field='gender', header=u'性别')
    nationality = Column(field='nationality', header=u'民族')
    age = Column(field='age', header=u'年龄')
    work_age = Column(field='work_age_display', header=u'工龄')
    local_age = Column(field='local_age', header=u'行龄')
    employee_type = Column(field='employee_type', header=u'员工性质')
    titles = Column(field='titles', header=u'职称')
    department = Column(field='department.name', header=u'机构名称')
    department_type = Column(field='department.type', header=u'机构类型')
    job = Column(field='job', header=u'岗位')
    political_status = Column(field='political_status', header=u'政治面貌')
    contract_start_date = Column(field='contracts.start_date', header=u'合同开始')
    contract_end_date = Column(field='contracts.end_date', header=u'合同结束')
    contract_duration = Column(field='contracts.duration', header=u'合同期限(年)')
    first_eduction_graduate_from = Column(field='first_eduction.graduate_from', header=u'毕业院校')
    first_eduction_qualification = Column(field='first_eduction.qualification', header=u'学历')
    first_eduction_major = Column(field='first_eduction.major', header=u'专业')

    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='EMPLOYEE:EMPLOYEE_DETAIL', args=(A('employee_number'), 'workexperience'),
                  image='/media/base_site/icons/edit.png',
                  image_title=u'查看详细')], sortable=False, )

    class Meta:
        id = u'员工花名册'
        model = Employee
        table_title = u'员工花名册'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs = {'class': 'bg-navy disabled color-palette'}


class TransferOrderList(Table):
    transfer_number = Column(field='transfer_number', header=u'调令编号')
    employee_number = Column(field='employee.employee_number', header=u'员工编号')
    name = Column(field='employee.name', header=u'员工姓名')
    old_department = Column(field='old_department.name', header=u'原部门')
    old_job = Column(field='old_job', header=u'原岗位')
    new_department = Column(field='new_department.name', header=u'现部门')
    new_job = Column(field='new_job', header=u'现岗位')
    transfer_date = Column(field='transfer_date', header=u'调用日期')
    new_department_salary_calculate_start_date = Column(field='new_department_salary_calculate_start_date',
                                                        header=u'新单位起薪日期')
    transfer_reason = Column(field='transfer_reason', header=u'调动原因')
    confirm = Column(field='confirm', header=u'同步到员工信息')

    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='EMPLOYEE:TRANSFER_DETAIL', args=(A('transfer_number'),),
                  image='/media/base_site/icons/edit.png',
                  image_title=u'查看详细')], sortable=False, )

    class Meta:
        id = u'员工调令表'
        model = TransferOrder
        table_title = u'员工调令表'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs = {'class': 'bg-navy disabled color-palette'}


class DimissionList(Table):
    id = Column(field='id',header = u'离职编号')
    employee = Column(field='employee',header=u'员工编号')
    name = Column(field='employee.name',header=u'员工姓名')
    dimission_date =Column(field='dimission_date',header=u'离职日期')
    record_date = Column(field='record_date',header=u'登记日期')
    reason = Column(field='reason',header=u'离职原因')
    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='EMPLOYEE:DIMISSION_DELETE', args=(A('id'),),
                  image='/media/base_site/icons/delete.png',
                  image_title=u'删除离职登记')], sortable=False, )

    class Meta:
        id = u'离职登记表'
        model = Dimission
        table_title = u'离职登记表'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs = {'class': 'bg-navy disabled color-palette'}


class DimissionEmployeeList(Table):
    employee_number = Column(field='employee_number', header=u'员工编号')
    name = Column(field='name', header=u'员工姓名')
    id_card = Column(field='identification_card', header=u'身份证号码')
    gender = Column(field='gender', header=u'性别')
    nationality = Column(field='nationality', header=u'民族')
    age = Column(field='age', header=u'年龄')
    work_age = Column(field='work_age_display', header=u'工龄')
    local_age = Column(field='local_age', header=u'行龄')
    employee_type = Column(field='employee_type', header=u'员工性质')
    titles = Column(field='titles', header=u'职称')
    department = Column(field='department.name', header=u'机构名称')
    department_type = Column(field='department.type', header=u'机构类型')
    job = Column(field='job', header=u'岗位')
    political_status = Column(field='political_status', header=u'政治面貌')
    contract_start_date = Column(field='contracts.start_date', header=u'合同开始')
    contract_end_date = Column(field='contracts.end_date', header=u'合同结束')
    contract_duration = Column(field='contracts.duration', header=u'合同期限(年)')
    first_eduction_graduate_from = Column(field='first_eduction.graduate_from', header=u'毕业院校')
    first_eduction_qualification = Column(field='first_eduction.qualification', header=u'学历')
    first_eduction_major = Column(field='first_eduction.major', header=u'专业')

    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='EMPLOYEE:DIMISSION_ADD', args=(A('employee_number'),),
                  image='/media/base_site/icons/add.png',
                  image_title=u'新增离职登记')], sortable=False, )

    class Meta:
        id = u'员工花名册'
        model = Employee
        table_title = u'员工花名册'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs = {'class': 'bg-navy disabled color-palette'}
