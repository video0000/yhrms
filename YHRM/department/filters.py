# -*-coding:utf-8-*-
import django_filters
from .models import Department


class DepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = Department
        fields = ['type', 'parent_structure']
