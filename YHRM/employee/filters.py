# -*-coding:utf-8-*-
import django_filters
from django import forms
from django.db import models
from django_filters.widgets import *

from department.models import Department
from .models import Employee

# query on method
# Employee.objects.all().filter(employee_number__in=[o.employee_number for o in q if o.age() == 29])


qualification_choices = ((u'小学', u'小学'),
                         (u'初中', u'初中'),
                         (u'高中', u'高中'),
                         ( u'中专', u'中专'),
                         (u'大专', u'大专'),
                         (u'本科', u'本科'),
                         (u'研究生', u'研究生'),
                         (u'博士', u'博士'))
contract_durtaion_choice = ((u'三年', u'三年'), (u'长期', u'长期'))

class EmployeeFilter(django_filters.FilterSet):

    first_eduction = django_filters.ChoiceFilter(label=u'第一学历', choices=qualification_choices,
                                                 method='first_eduction_filter')
    contracts_duration = django_filters.ChoiceFilter(label=u'合同期限', choices=contract_durtaion_choice,
                                                 method='contracts_duration_filter')
    age = django_filters.NumericRangeFilter(label=u'年龄', method='age_filter', )
    work_age = django_filters.NumericRangeFilter(label=u'工龄', method='work_age_filter', )
    local_age = django_filters.NumericRangeFilter(label=u'行龄', method='local_age_filter', )

    class Meta:
        model = Employee
        fields = ['department', 'department__type', 'gender', 'employee_type', 'political_status',
                 'contracts_duration', 'first_eduction', 'age', 'work_age', 'local_age']

    @staticmethod
    def contracts_duration_filter(self, qs, value):
        q = self
        if value is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value == o.contracts.duration])

    @staticmethod
    def first_eduction_filter(self, qs, value):
        q = self
        if value is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value == o.first_eduction_qualification()])

    @staticmethod
    def age_filter(self, qs, value):
        q = self
        if value.start is not None and value.stop is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value.start <= o.age() <= value.stop])
        elif value.start is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value.start <= o.age()])
        elif value.stop is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if o.age() <= value.stop])
        else:
            return q

    @staticmethod
    def work_age_filter(self, qs, value):
        q = self
        if value.start is not None and value.stop is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value.start <= o.work_age() <= value.stop])
        elif value.start is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value.start <= o.work_age()])
        elif value.stop is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if o.work_age() <= value.stop])
        else:
            return q

    @staticmethod
    def local_age_filter(self, qs, value):
        q = self
        if value.start is not None and value.stop is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value.start <= o.local_age() <= value.stop])
        elif value.start is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if value.start <= o.local_age()])
        elif value.stop is not None:
            return q.filter(
                employee_number__in=[o.employee_number for o in q if o.local_age() <= value.stop])
        else:
            return q
