# -*-coding:utf-8-*-
from django import forms
from .models import Department


class DepartmentAddForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['', ]


class DepartmentChangeForm(forms.ModelForm):
    class Meta:
        model = Department
        exclude = ['department_number', ]
