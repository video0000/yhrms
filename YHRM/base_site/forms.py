# -*-coding:utf-8-*-
from PIL import Image
from django import forms
from django.contrib.auth.forms import UserChangeForm

from base_site.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['username', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'last_login',
                   'email', 'user_permissions', 'groups', 'password', 'date_joined', ]


class PasswordChangeForm(forms.Form):
    oldpassword = forms.CharField(
        required=True,
        label=u"原密码",
        error_messages={'required': u'请输入原密码'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"原密码",
            }
        ),
    )
    newpassword1 = forms.CharField(
        required=True,
        label=u"新密码",
        error_messages={'required': u'请输入新密码'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"新密码",
            }
        ),
    )
    newpassword2 = forms.CharField(
        required=True,
        label=u"确认密码",
        error_messages={'required': u'请再次输入新密码'},
        widget=forms.TextInput(
            attrs={
                'placeholder': u"确认密码",
            }
        ),
    )

    def clean(self):
        if not self.is_valid():
            raise forms.ValidationError(u"密码信息不正确")
        elif self.cleaned_data['newpassword1'] <> self.cleaned_data['newpassword2']:
            raise forms.ValidationError(u"两次输入的新密码不一样")
        elif self.cleaned_data['oldpassword'] == self.cleaned_data['newpassword1']:
            raise forms.ValidationError(u'新密码与原密码相同')
        else:
            cleaned_data = super(PasswordChangeForm, self).clean()
        return cleaned_data


class MyAvatarChangeForm(forms.Form):
    avatar_to_change = forms.ImageField(
        label=u'头像',
        required=False
    )


class MyProfileChangeForm(forms.Form):
    name_cn=forms.CharField(
        label=u'中文名',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': u"中文名",
            }
        ),
    )
    telephone = forms.CharField(
        label=u'电话号码',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': u"电话号码",
            }
        ),
    )
    qq = forms.CharField(
        label=u'QQ号码',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': u"QQ号码",
            }
        ),
    )
    email = forms.CharField(
        label=u'电子邮件地址',
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': u"电子邮件地址",
            }
        ),
    )

