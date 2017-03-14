# -*-coding:utf-8-*-
from django import forms
from .models import *


class LeaveAddForm(forms.ModelForm):
    def clean(self):
        if count_holiday(self.cleaned_data['start_date'], self.cleaned_data['end_date']) > leaveDaysLeft(
                self.cleaned_data['employee']):
            raise forms.ValidationError(u"休假天数超过剩余可休假天数")

    class Meta:
        model = Leave
        exclude = ['', ]


class LeaveChangeForm(forms.ModelForm):
    class Meta:
        model = Leave
        exclude = ['id','employee','start_date','end_date']
