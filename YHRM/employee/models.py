# -*-coding:utf-8-*-
import datetime
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils.html import format_html
from simple_history.models import HistoricalRecords
from django.utils.timezone import now

from department.models import Department

employee_gender_choice = ((u'男', u'男'),
                          (u'女', u'女'))
political_status_choice = ((u'党员', u'党员'),
                           (u'群众', u'群众'),
                           (u'其他民主党派', u'其他民主党派'))

employee_type_choices = ((u'领导班子', u'领导班子'),
                         (u'中层正职', u'中层正职'),
                         (u'中层副职', u'中层副职'),
                         (u'正式在岗员工', u'正式在岗员工'),
                         (u'代办员', u'代办员'),
                         (u'离岗休养干部', u'离岗休养干部'),
                         (u'离岗休养员工', u'离岗休养员工'),
                         (u'内退', u'内退'))


# Create your models here.
class Employee(models.Model):
    employee_number = models.CharField(verbose_name=u'员工编号', primary_key=True, max_length=20, blank=False, null=False)
    name = models.CharField(verbose_name=u'员工姓名', max_length=50, blank=True, null=True, )
    atatar = models.ImageField(verbose_name=u'照片', upload_to='employee/avatar/', default='employee/avatar/default.jpg',
                               blank=True, null=True)
    gender = models.CharField(verbose_name=u'性别', blank=True, null=True, max_length=20, choices=employee_gender_choice,
                              default='male')
    nationality = models.CharField(verbose_name=u'民族', default=u'汉族', max_length=10, blank=True, null=True, )
    birthday = models.DateField(verbose_name=u'生日', blank=False, null=False, )
    date_of_start_working = models.DateField(verbose_name=u'参加工作时间', blank=True, null=True, )
    date_of_joined_bccb = models.DateField(verbose_name=u'到商工作时间', blank=True, null=True, )
    employee_type = models.CharField(verbose_name=u'员工性质', blank=True, null=True, max_length=20,
                                     choices=employee_type_choices, default='Formal Staff')
    titles = models.CharField(verbose_name=u'职称', max_length=50, blank=True, null=True, )
    department = models.ForeignKey(Department, verbose_name=u'部门', blank=True, null=True, related_name='employees')
    job = models.CharField(verbose_name=u'岗位', max_length=50, blank=True, null=True, )
    political_status = models.CharField(verbose_name=u'政治面貌', max_length=50, blank=True, null=True,
                                        choices=political_status_choice)
    political_joined_date = models.DateField(verbose_name=u'入党日期', blank=True, null=True)

    identification_card = models.CharField(verbose_name=u'身份证号码', blank=True, null=True, max_length=20)
    home_address = models.CharField(verbose_name=u'家庭住址', max_length=100, blank=True, null=True, )

    def avatar_preview(self):
        try:
            url = self.atatar.url
        except:
            url = 'employee/avatar/default.jpg'
        return format_html('<img src="%s" width="50px" />' % self.atatar.url)

    avatar_preview.short_description = u"照片预览"

    def __unicode__(self):
        return self.employee_number

    def age(self):
        try:
            age = (datetime.date.today() - self.birthday).days // 365
        except:
            age = u'无法计算'
        return age

    age.short_description = u'年龄'

    def work_age(self):
        try:
            age = (datetime.date.today() - self.date_of_start_working).days // 365
            if age == 0 or age == 9 or age == 19 :
                age = round((0.0 + (datetime.date.today() - self.date_of_start_working).days) / 365,2)
        except:
            age = u'无法计算'
        return age
    def work_age_display(self):
        u"""
        显示要整数
        :return:
        """
        return int(self.work_age())

    work_age.short_description = u'工龄'

    def local_age(self):
        try:
            age = (datetime.date.today() - self.date_of_joined_bccb).days // 365
        except:
            age = u'无法计算'
        return age

    local_age.short_description = u'行龄'

    # def work_age_float(self):
    #     try:
    #         age = 0.0 + (datetime.date.today() - self.date_of_start_working).days / 365
    #     except:
    #         age = u'无法计算'
    #     return age
    #
    # def local_age_float(self):
    #     try:
    #         age = 0.0 + (datetime.date.today() - self.date_of_joined_bccb).days / 365
    #     except:
    #         age = u'无法计算'
    #     return age

    def first_eduction(self):
        try:
            eduction = self.eductions.filter(type='first')[0]
            return eduction
        except:
            return u'没有找到第一学历信息！'

    first_eduction.short_description = u'第一学历'

    def first_eduction_qualification(self):
        try:
            eduction = self.eductions.filter(type='first')[0].qualification
            return eduction
        except:
            return u'没有找到第一学历信息！'

    def leaveDaysTotal(self):
        """计算本年度可休假天数"""
        employee = self

        if self.local_age() < 1:
            return 0
        elif self.work_age < 1:
            return int(self.work_age() * 5)
        elif 1 <= self.work_age() < 9:
            print 1
            return 5
        elif 9 <= self.work_age() < 10:
            print 2
            return 5 + int((self.work_age() - 9)*5)
        elif 10 < self.work_age() < 19:
            return 10
        elif 19 <= self.work_age() < 20:
            return 10 +  int((self.work_age() - 19)*5)
        else:
            return 15

    def leaveDaysLeft(self):
        """计算剩余可休假天数"""
        employee = self
        leavedays = 0
        for i in employee.leaves.filter(start_date__year=datetime.date.today().year):
            leavedays = leavedays + i.duration()
        return self.leaveDaysTotal() - leavedays

    leaveDaysLeft.short_description = u'年度剩余休假天数'
    history = HistoricalRecords()

    class Meta:
        verbose_name = u'员工信息'
        verbose_name_plural = u'员工信息'
        ordering = ['employee_number', ]


contract_durtaion_choice = ((u'三年', u'三年'), (u'长期', u'长期'))


class Contract(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'员工编号', related_name='contracts')
    start_date = models.DateField(verbose_name=u'开始日期', blank=False, null=False, )
    end_date = models.DateField(verbose_name=u'结束日期', blank=True, null=True)
    duration = models.CharField(verbose_name=u'合同期限', choices=contract_durtaion_choice, blank=False, null=False,
                                max_length=50, default='long_term')
    pdf = models.FileField(verbose_name=u'合同影印', blank=True, null=True, upload_to='employee/contract')
    history = HistoricalRecords()

    # def duration(self):
    #     return (self.end_date - self.start_date).days // 365

    class Meta:
        verbose_name = u'合同信息'
        verbose_name_plural = u'合同信息'
        ordering = ['employee', '-start_date']


eduction_choices = ((u'第一学历', u'第一学历'), (u'现学历', u'现学历'), (u'其他类型学历', u'其他类型学历'))
qualification_choices = ((u'小学', u'小学'),
                         (u'初中', u'初中'),
                         (u'高中', u'高中'),
                         (u'中专', u'中专'),
                         (u'大专', u'大专'),
                         (u'本科', u'本科'),
                         (u'研究生', u'研究生'),
                         (u'博士', u'博士'))


class Eduction(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'员工编号', related_name='eductions', )
    start_date = models.DateField(verbose_name=u'开始日期', blank=False, null=False)
    end_date = models.DateField(verbose_name=u'结束日期', blank=False, null=False)
    qualification = models.CharField(verbose_name=u'学历', blank=False, null=False, max_length=50,
                                     choices=qualification_choices, default='Undergraduate')
    degree = models.CharField(verbose_name=u'学位', blank=True, null=True, max_length=50)
    major = models.CharField(verbose_name=u'专业', blank=True, null=True, max_length=50)
    graduate_from = models.CharField(verbose_name=u'毕业院校', blank=False, null=False, max_length=200)
    type = models.CharField(verbose_name=u"学历类型", blank=False, null=False, max_length=50, choices=eduction_choices)
    history = HistoricalRecords()

    def __unicode__(self):
        return self.graduate_from + ':' + self.get_qualification_display() + '-' + self.degree

    class Meta:
        verbose_name = u'学历信息'
        verbose_name_plural = u'学历信息'
        ordering = ['employee', '-start_date']


class WorkExperience(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'员工编号', related_name=u'work_experiences')
    start_date = models.DateField(verbose_name=u'开始日期', blank=False, null=False)
    end_date = models.DateField(verbose_name=u'结束日期', blank=True, null=True)
    department = models.ForeignKey(Department, blank=False, null=False, verbose_name=u'部门')
    job = models.CharField(verbose_name=u'岗位', max_length=50, blank=True, null=True, )
    transfer_order_number = models.CharField(verbose_name=u'调令编号', max_length=50, blank=True, null=True, )
    history = HistoricalRecords()

    class Meta:
        verbose_name = u'本单位工作经历'
        verbose_name_plural = u'本单位工作经历'
        ordering = ['employee', '-start_date']


class RelationShip(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'员工编号', related_name=u'relationships')
    name = models.CharField(verbose_name=u'姓名', max_length=50, blank=False, null=False)
    relation = models.CharField(verbose_name=u'与本人关系', max_length=50, blank=False, null=False)
    birthday = models.DateField(verbose_name=u'生日', blank=True, null=True)
    political_status = models.CharField(verbose_name=u'政治面貌', max_length=50, blank=True, null=True, )
    graduate_from = models.CharField(verbose_name=u'毕业院校及专业', blank=True, null=True, max_length=200)
    job = models.CharField(verbose_name=u'工作单位及职务', max_length=50, blank=True, null=True, )
    history = HistoricalRecords()

    class Meta:
        verbose_name = u'社会关系'
        verbose_name_plural = u'社会关系'


class Remark(models.Model):
    employee = models.OneToOneField(Employee, verbose_name=u'员工编号', related_name=u'remarks')
    remark = models.TextField(verbose_name=u'其他需要说明情况')
    history = HistoricalRecords()

    class Meta:
        verbose_name = u'其他需要说明情况'
        verbose_name_plural = u'其他需要说明情况'


class TransferOrder(models.Model):
    employee = models.ForeignKey(Employee, verbose_name=u'员工编号', related_name=u'transferorders_by_employee')
    transfer_number = models.CharField(verbose_name=u'调令号', primary_key=True, max_length=20, blank=False, null=False)
    old_department = models.ForeignKey(Department, verbose_name=u'原部门', related_name='transfer_order_by_old_department')
    old_job = models.CharField(verbose_name=u'原岗位', max_length=50, blank=True, null=True, )
    new_department = models.ForeignKey(Department, verbose_name=u'现部门', related_name='transfer_order_by_new_department')
    new_job = models.CharField(verbose_name=u'现岗位', max_length=50, blank=True, null=True, )
    transfer_date = models.DateField(verbose_name=u'调动日期')
    new_department_salary_calculate_start_date = models.DateField(verbose_name=u'新单位起薪日期')
    transfer_reason = models.TextField(verbose_name=u'调动原因', blank=True, null=True, )
    confirm = models.BooleanField(verbose_name=u'同步到员工信息', default=False)
    history = HistoricalRecords()

    # def save(self, *args, **kwargs):
    #     self.employee.department = self.new_department
    #     self.employee.job = self.new_job
    #     self.employee.save()
    #     workexperience = WorkExperience(employee=self.employee, start_date=self.transfer_date,
    #                                     department=self.new_department, job=self.new_job)
    #     workexperience.save()
    #     super(TransferOrder, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u'调令'
        verbose_name_plural = u'调令'
        ordering = ['employee', '-transfer_date']


class Dimission(models.Model):
    employee = models.OneToOneField(Employee, verbose_name=u'员工编号', related_name='dimissions')
    dimission_date = models.DateField(verbose_name=u'离职日期', blank=False, null=False)
    record_date = models.DateField(verbose_name=u'登记日期', auto_now_add=True)
    reason = models.TextField(verbose_name=u'离职原因')
    history = HistoricalRecords()

    class Meta:
        verbose_name = u'离职'
        verbose_name_plural = u'离职'
        ordering = ['-record_date']
