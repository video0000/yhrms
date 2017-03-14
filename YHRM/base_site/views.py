# -*-coding:utf-8-*-
import os

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from PIL import Image
from base_site.forms import PasswordChangeForm, MyAvatarChangeForm, MyProfileChangeForm



@login_required
def index(request):
    return render(request, 'base_site/index.html')


@login_required
def my_profile(request):

    return render(request, 'base_site/account/account_detail.html', )


@login_required
def change_my_password(request):
    if request.method == 'GET':
        form = PasswordChangeForm()
        return render(request, 'base_site/account/change_password.html', {'form': form,})
    else:
        form = PasswordChangeForm(request.POST)
        if form.is_valid():
            username = request.user.username
            oldpassword = request.POST.get('oldpassword', '')
            user = auth.authenticate(username=username, password=oldpassword)
            if user is not None and user.is_active:
                newpassword = request.POST.get('newpassword1', '')
                user.set_password(newpassword)
                user.save()
                return HttpResponseRedirect(reverse('BP_MYPROFILE'))
            else:
                return render(request, 'base_site/account/change_password.html',
                              {'form': form})
                # return render_to_response('changepwd.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))
        else:
            return render(request, 'base_site/account/change_password.html', {'form': form})
            # return render_to_response('changepwd.html', RequestContext(request, {'form': form,}))


def IsValidImage(file):
    u"""判断文件图片格式是否正确"""
    valid = True
    try:
        Image.open(file).verify()
    except:
        valid = False
    return valid

@login_required
def change_my_avatar(request):
    user = request.user
    if request.method == 'GET':
        form = MyAvatarChangeForm()
        return render(request, 'base_site/account/change_avatar.html', {'form': form,})
    else:
        form = MyAvatarChangeForm(request.POST)
        if form.is_valid():
            if IsValidImage(request.FILES['avatar_to_change']):
                form = MyAvatarChangeForm()
                if os.path.exists(request.user.avatar.path):
                    os.remove(request.user.avatar.path)
                user.avatar = request.FILES['avatar_to_change']
                user.save()
                return HttpResponseRedirect(reverse('BP_MYPROFILE'))
            form = MyAvatarChangeForm(request.POST)
            return render(request, 'base_site/account/change_avatar.html', {'form': form, 'file_is_not_a_picture': True})
        return render(request, 'base_site/account/change_avatar.html', {'form': form,})


@login_required
def change_my_profile(request):
    if request.method == "GET":
        form = MyProfileChangeForm(request.GET)
        return render(request, 'base_site/account/change_profile.html', {'form': form})
    else:
        user = request.user
        if request.POST.get('name_cn', "") <> "": user.name_cn = request.POST.get('name_cn', "")
        if request.POST.get('qq', "") <> "": user.qq = request.POST.get('qq', "")
        if request.POST.get('email', "") <> "": user.email = request.POST.get('email', "")
        if request.POST.get('telephone', "") <> "": user.telephone = request.POST.get('telephone', "")
        user.save()
        return HttpResponseRedirect(reverse('BP_MYPROFILE'))


def login(request):
    if request.method == 'GET':
        return render(request, 'base_site/login/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('BP_INDEX'))
        else:
            return render(request, 'base_site/login/login.html',
                          {'password_is_wrong': True})


def logout(request):
    auth.logout(request)
    return render(request, 'base_site/login/logout.html')
