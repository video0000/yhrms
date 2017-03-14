# coding=utf-8
from django.db import models
from simple_history.models import HistoricalRecords

department_type_choice = (
(u"总行", u"总行"), (u"总行班子", u"总行班子"), (u"总行业务部室", u"总行业务部室"), (u"总行其他部室", u"总行其他部室"), (u"支行", u"支行"),)


# Create your models here.
class Department(models.Model):
    department_number = models.CharField(verbose_name='机构编号', primary_key=True, max_length=20,
                                         blank=False, null=False)

    name = models.CharField(verbose_name='机构名称', max_length=50, blank=True, null=True)
    type = models.CharField(verbose_name='机构类型', max_length=20, blank=True, null=True,
                            choices=department_type_choice, default='')
    address = models.CharField(verbose_name='机构地址', max_length=200, blank=True, null=True)
    phone = models.CharField(verbose_name='机构电话', max_length=20, blank=True, null=True)
    parent_structure = models.ForeignKey('Department', verbose_name='上级机构', related_name='children', max_length=50,
                                         blank=True, null=True, )
    history = HistoricalRecords()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = '机构信息'
        ordering = ['department_number', ]
