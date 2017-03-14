# -*-coding:utf-8 -*-
from django.db import models
import datetime

# Create your models here.
from django.shortcuts import get_object_or_404
from simple_history.models import HistoricalRecords

from employee.models import Employee

leave_type_choices = ((u'年假', u'年假'), (u'事假', u'事假'), (u'病假', u'病假'),(u'婚假',u'婚假'),
 (u'产假及护理假', u'产假及护理假'),(u'哺乳假',u'哺乳假'),(u'丧假',u'丧假'),(u'探亲假',u'探亲假'))


def leaveDaysTotal(employee_number):
    """计算本年度可休假天数"""
    employee = get_object_or_404(Employee, employee_number=employee_number)
    if employee.local_age() < 1:
        return 0
    elif employee.work_age < 1:
        return int(employee.work_age() * 5)
    elif 1 <= employee.work_age() < 9:
        return 5
    elif 9 <= employee.work_age() < 10:
        return 5 +  int((employee.work_age_float - 9)*5)
    elif 10 < employee.work_age() < 19:
        return 10
    elif 19 <= employee.work_age() < 20:
        return 10 + int((employee.work_age() - 19)*5)
    else:
        return 15


def leaveDaysLeft(employee_number):
    """计算剩余可休假天数"""
    employee = get_object_or_404(Employee, employee_number=employee_number)
    leavedays = 0
    for i in employee.leaves.filter(start_date__year=date.today().year).filter(type=u'年假'):
        leavedays = leavedays + i.duration()
    return leaveDaysTotal(employee_number) - leavedays


class Leave(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'员工编号', related_name='leaves')
    leave_type = models.CharField(verbose_name=u'休假类型', choices=leave_type_choices,
                                  default=u'年假', max_length=20)
    start_date = models.DateField(verbose_name=u'开始日期')
    end_date = models.DateField(verbose_name=u'结束日期')
    reason = models.TextField(verbose_name=u'休假原因', blank=+True, null=True)
    history = HistoricalRecords()

    def duration(self):
        return count_holiday(self.start_date, self.end_date)

    duration.short_description = u'休假天数'

    class Meta:
        verbose_name = u'休假信息'
        verbose_name_plural = u'休假信息'
        ordering = ['employee', '-start_date']


class Holiday(models.Model):
    name = models.CharField(verbose_name=u'节日名称', max_length=250)
    start_date = models.DateField(verbose_name=u'开始日期')
    end_date = models.DateField(verbose_name=u'结束日期')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'节日信息'
        verbose_name_plural = u'节日信息'
        ordering = ['-start_date', ]


class Exchanging_Holiday(models.Model):
    holiday = models.ForeignKey(Holiday, verbose_name=u'节日信息', related_name='exchanging_holiday')
    date = models.DateField(verbose_name=u'串休上班日期')

    def __unicode__(self):
        return self.holiday.name

    class Meta:
        verbose_name = u'串休上班信息'
        verbose_name_plural = u'串休上班信息'
        ordering = ['-date', ]


from datetime import date, datetime, timedelta


def is_holiday(date):
    """
    计算日期是否为节假日，没有采用网络api的方式，而是将节假日信息存入数据库
    :param date:
    :return:
    """
    weekday = date.weekday()
    holiday_start_date_list = Holiday.objects.values_list('start_date')
    holiday_end_date_list = Holiday.objects.values_list('end_date')
    length = len(holiday_start_date_list)
    holiday_exchanging_date = Exchanging_Holiday.objects.values_list('date')
    holiday_exchanging_date_list = []
    for i in holiday_exchanging_date:
        holiday_exchanging_date_list.append(i[0])
    for i in range(length):
        if holiday_start_date_list[i][0] <= date <= holiday_end_date_list[i][0]:
            return True
    if weekday in [5, 6]:
        if not date in holiday_exchanging_date_list:
            return True
    return False


def count_holiday(start_date, end_date):
    """
    计算日期间隔中共有多少个工作日
    :param start_date:
    :param end_date:
    :return:
    """
    count = (end_date - start_date).days
    for i in range(count):
        if is_holiday(start_date + timedelta(i)):
            count -= 1
    return count
