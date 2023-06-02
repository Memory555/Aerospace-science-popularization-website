import random

from django.shortcuts import render
from django.http import HttpResponse
from polls import models
from django.http import HttpResponseRedirect

# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u = request.POST.get("u", '')
    p = request.POST.get("p", '')

    if u and p:  # 用于判断是否输入完整
        c = models.PollsStudentinfo.objects.filter(stu_name=u, stu_pwd=p).count()
        if c >= 1:
            # return HttpResponse("登录成功！")
            return HttpResponseRedirect("/polls/tosuccess/")
        else:
            return HttpResponse("账号或密码错误！请返回上一级重新登录")
    else:
        return HttpResponse("请返回上一级重新登录，重新输入账号和密码！")

#渲染注册界面
def toregister_view(request):
    return render(request,'register.html')  # 渲染一个页面

# 点击注册后的逻辑判断
def register_view(request):
    u = request.POST.get("u", '')
    p = request.POST.get("p", '')
    e = request.POST.get("e", '')
    ph = request.POST.get("ph", '')
    b = request.POST.get("b", '')
    if u and p and ph and e and b:
        stu = models.PollsStudentinfo(stu_id = str(random.randrange(1111,9999)),stu_name = u,stu_pwd = p,stu_email = e,stu_phone = ph,stu_data = b)
        stu.save()
        # return HttpResponse("注册成功！")
        return HttpResponseRedirect("/polls/")
    else:
        return HttpResponse("请返回上一级输入完整的账号和密码！")
# str(stu_id = random.randrange(111,999)),

#渲染忘记密码界面
def toforget_view(request):
    return render(request,'forget.html')  # 渲染一个页面

def tosuccess_view(request):
    return HttpResponseRedirect("/polls/success")

# 渲染成功登录界面
def success_view(request):
    return render(request,'shouye.html')  # 渲染一个页面

def tohelp_view(request):
    return HttpResponseRedirect("/polls/help")

def help_view(request):
    return render(request,'help.html')

def tomy_view(request):
    return HttpResponseRedirect("/polls/my")

def my_view(request):
    return render(request,'myaccount.html')

def tonewguide_view(request):
    return HttpResponseRedirect("/polls/newguide")

def newguide_view(request):
    return render(request,'newGuider.html')

def toshuju_view(request):
    return HttpResponseRedirect("/polls/shuju")

def shuju_view(request):
    return render(request,'shuju.html')

def toknow_view(request):
    return HttpResponseRedirect("/polls/know")

def know_view(request):
    return render(request,'knowledge.html')

def yusuan_view(request):
    return render(request,'yusuan.html')

def zme_view(request):
    return render(request,'zme.html')

def China_view(request):
    return render(request,'China.html')

def zm_view(request):
    return render(request,'zm.html')