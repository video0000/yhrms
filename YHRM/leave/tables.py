# -*-coding:utf-8-*-
from tablib.packages.omnijson.core import options

from employee.admin import DimissionAdmin
from leave.models import Leave
from table.utils import A

from employee.models import Employee
from table.columns import Column
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table import Table


class LeaveEmployeeList(Table):
    employee_number = Column(field='employee_number', header=u'员工编号')
    name = Column(field='name', header=u'员工姓名')
    id_card = Column(field='identification_card', header=u'身份证号码')
    age = Column(field='age', header=u'年龄')
    work_age = Column(field='work_age_display', header=u'工龄')
    local_age = Column(field='local_age', header=u'行龄')
    employee_type = Column(field='employee_type', header=u'员工性质')
    titles = Column(field='titles', header=u'职称')
    department = Column(field='department.name', header=u'机构名称')
    department_type = Column(field='department.type', header=u'机构类型')
    job = Column(field='job', header=u'岗位')
    leaveDaysTotal = Column(field='leaveDaysTotal', header=u'年总休假')
    leaveDaysLeft = Column(field='leaveDaysLeft', header=u'年余休假')
    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='LEAVE:LEAVE_ADD', args=(A('employee_number'),),
                  image='/media/base_site/icons/add.png',
                  image_title=u'休假登记')], sortable=False, )

    class Meta:
        id = u'休假员工表'
        model = Employee
        table_title = u'休假员工表'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs = {'class': 'bg-navy disabled color-palette'}


class LeaveList(Table):
    id = Column(field='id', header=u'休假登记编号')
    employee = Column(field='employee.employee_number', header=u'员工编号')
    name = Column(field='employee.name', header=u'员工姓名')
    leave_type = Column(field='leave_type', header=u'休假类型')
    start_date = Column(field='start_date', header=u'开始日期')
    end_date = Column(field='end_date', header=u'结束日期')
    duration = Column(field='duration', header=u'休假天数')
    reason = Column(field='reason', header=u'休假原因')
    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='LEAVE:LEAVE_CHANGE', args=(A('id'),),
                  image='/media/base_site/icons/edit.png',
                  image_title=u'修改休假记录')], sortable=False, )
    link2 = LinkColumn(header=u'', links=[
        ImageLink(viewname='LEAVE:LEAVE_DELETE', args=(A('id'),),
                  image='/media/base_site/icons/delete.png',
                  image_title=u'删除休假记录')], sortable=False, )

    class Meta:
        id = u'员工休假表'
        model = Leave
        table_title = u'员工休假表'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs = {'class': 'bg-navy disabled color-palette'}
