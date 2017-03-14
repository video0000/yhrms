# -*-coding:utf-8-*-
from tablib.packages.omnijson.core import options

from table.utils import A

from .models import Department

from table.columns import Column
from table.columns.linkcolumn import LinkColumn, Link, ImageLink
from table import Table


class DepartmentList(Table):
    department_number = Column(field='department_number', header=u'机构编号')
    name = Column(field='name', header=u'机构名称')
    type = Column(field='type', header=u'机构类型')
    address = Column(field='address', header=u'机构地址')
    phone = Column(field='phone', header=u'机构电话')
    parent_structure = Column(field='parent_structure', header=u'上级机构')
    link = LinkColumn(header=u'', links=[
        ImageLink(viewname='DEPARTMENT:DEPARTMENT_DETAIL', args=(A('department_number'),),
                  image='/media/base_site/icons/edit.png',
                  image_title=u'查看详细')], sortable=False, )

    class Meta:
        id = u'机构信息表'
        model = Department
        table_title = u'机构信息表'
        attrs = {'class': 'table-bordered table-hover table-striped'}
        thead_attrs ={'class': 'bg-navy disabled color-palette'}
