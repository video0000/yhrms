# -*-coding:utf-8-*-
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.utils.html import format_html

# class UserProfile(models.Model):
#     user=models.OneToOneField(User)
#     avatar = models.ImageField(verbose_name=u"头像",
#                                blank=True, null=True,
#                                upload_to='base_site/user_profile/avatar/',
#                                default='base_site/user_profile/avatar/default.jpg')
#
#     def avatar_preview(self):
#         return format_html('<img src="%s" width="50px" />' % self.avatar.url)
#
#     avatar_preview.short_description = u"头像预览"
from simple_history.models import HistoricalRecords


class UserProfile(AbstractUser):
    """
    继承AbstractUser类，实际上django的User也是继承他，我用自己的类代替django默认的User
    """
    name_cn = models.CharField(verbose_name="中文姓名", max_length=50, blank=True, null=True)
    telephone = models.CharField(verbose_name="电话号码", max_length=50, blank=True, null=True)
    qq = models.CharField(verbose_name='QQ号码', max_length=50, blank=True, null=True)
    avatar = models.ImageField(verbose_name=u"头像",
                               blank=True, null=True,
                               upload_to='base_site/user_profile/avatar/',
                               default='base_site/user_profile/avatar/default.jpg')

    def avatar_preview(self):
        return format_html('<img src="%s" width="50px" />' % self.avatar.url)

    avatar_preview.short_description = u"头像预览"

    class Meta:
        verbose_name = u'用户资料'
        verbose_name_plural = u'用户资料'
