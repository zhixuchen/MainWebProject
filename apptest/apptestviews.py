from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from apptest.models import Appcase, Appcasestep


# Create your views here.
# # app 用例管理
# @login_required
# def appcase_manage(request):
#     appcase_list = Appcase.objects.all()
#     username = request.session.get('user', '') # 读取浏览器登录 Session
#     return render(request,"appcase_manage.html",{"user": username,"appcases":appcase_list})
# # App 用例测试步骤
# @login_required
# def appcasestep_manage(request):
#     username = request.session.get('user', '')
#     appcasestep_list = Appcasestep.objects.all()
#     return render(request, "appcasestep_manage.html", {"user": username,"appcasesteps": appcasestep_list})

@login_required
def appsearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_appcasename = request.GET.get("appcasename", "")
    appcase_list = Appcase.objects.filter(appcasename__icontains=search_appcasename)
    return render(request, 'appcase_manage.html', {"user": username, "appcases": appcase_list})


# 搜索功能
@login_required
def appstepsearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_appcasename = request.GET.get("appcasename", "")
    appcasestep_list = Appcasestep.objects.filter(appcasename__icontains=search_appcasename)
    return render(request, 'appcasestep_manage.html', {"user": username, "appcasesteps": appcasestep_list})


# App 测试用例管理
@login_required
def appcase_manage(request):
    appcase_list = Appcase.objects.all()
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    paginator = Paginator(appcase_list, 8)  # 生成 paginator 对象,设置每页显示 8 条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数,默认为第 1 页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        appcase_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        appcase_list = paginator.page(1)  # 如果输入的页数不是整数则显示第 1 页的内容
    except EmptyPage:
        appcase_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中则显示最后一页的内容
    appcase_count = Appcase.objects.all().count()  # 统计产品数
    return render(request, "appcase_manage.html", {"user": username, "appcases":
        appcase_list, "appcasecounts": appcase_count})  # 把值赋给 appcasecounts 变量


# App 测试步骤管理
# 步骤管理
@login_required
def appcasestep_manage(request):
    username = request.session.get('user', '')
    appcasestep_list = Appcasestep.objects.all()
    appcaseid = request.GET.get('appcase.id', None)
    appcase = Appcase.objects.get(id=appcaseid)
    appcasestep_list = Appcasestep.objects.all()
    return render(request, "appcasestep_manage.html",
                  {"user": username, "appcase": appcase, "appcasesteps": appcasestep_list})
