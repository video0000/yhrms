# -*-coding:utf-8-*-
from django import forms
from .models import *


class EmployeeChangeFormBasicInformation(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['employee_number', 'atatar']


class EmployeeChangeFormAvatar(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['atatar', ]


class EmployeeChangeFormContract(forms.ModelForm):
    class Meta:
        model = Contract
        exclude = ['employee', ]


class EmployeeAddFormContract(forms.ModelForm):
    class Meta:
        model = Contract
        exclude = ['', ]


class EmployeeChangeFormRemark(forms.ModelForm):
    class Meta:
        model = Remark
        exclude = ['employee', ]


class EmployeeAddFormRemark(forms.ModelForm):
    class Meta:
        model = Remark
        exclude = ['', ]


class EmployeeChangeFormEduction(forms.ModelForm):
    class Meta:
        model = Eduction
        exclude = ['id', 'employee']


class EmployeeAddFormEduction(forms.ModelForm):
    class Meta:
        model = Eduction
        exclude = ['', ]


class EmployeeChangeFormWorkExperience(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['id', 'employee', 'transfer_order_number']


class EmployeeAddFormWorkExperience(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['transfer_order_number', ]


class EmployeeChangeFormRelationShip(forms.ModelForm):
    class Meta:
        model = RelationShip
        exclude = ['id', 'employee']


class EmployeAddFormRelationShip(forms.ModelForm):
    class Meta:
        model = RelationShip
        exclude = ['', ]


class TransferOrderChangeForm(forms.ModelForm):
    class Meta:
        model = TransferOrder
        exclude = ['transfer_number', 'employee', 'confirm', 'confirm']


class TransferOrderAddForm(forms.ModelForm):
    class Meta:
        model = TransferOrder
        exclude = ['', ]


class DimissionAddForm(forms.ModelForm):
    class Meta:
        model = Dimission
        exclude = ['', ]
