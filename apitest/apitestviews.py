# Create your views here.
import pymysql
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from apitest.models import Apitest, Apistep, Apis
from MainWebProject import function



# 测试报告
@login_required
def test_report(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    apis_count = Apis.objects.all().count()  # 统计接口数
    mysql=function.mysql()
    cursor=mysql.cursor
    sql1 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=1'
    aa = cursor.execute(sql1)
    apis_pass_count = [row[0] for row in cursor.fetchmany(aa)][0]
    sql2 = 'SELECT count(id) FROM apitest_apis WHERE apitest_apis.apistatus=0'
    bb = cursor.execute(sql2)
    apis_fail_count = [row[0] for row in cursor.fetchmany(bb)][0]
    mysql.conect_close()
    return render(request, "report.html",
                  {"user": username, "apiss": apis_list, "apiscounts": apis_count, "apis_pass_counts": apis_pass_count,
                   "apis_fail_counts": apis_fail_count})  # 把值赋给apiscounts





# 搜索功能
@login_required
def apisearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 session
    search_apitestname = request.GET.get("apitestname", "")
    apitest_list = Apitest.objects.filter(apitestname__icontains=search_apitestname)
    return render(request, 'apitest_manage.html', {"user": username, "apitests": apitest_list})


@login_required
def apissearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_apiname = request.GET.get("apiname", "")
    apis_list = Apis.objects.filter(apiname__icontains=search_apiname)
    return render(request, 'apis_manage.html', {"user": username, "apiss": apis_list})


@login_required
def apitest_manage(request):
    apitest_list = Apitest.objects.all()  # 获取所有接口测试用例
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    paginator = Paginator(apitest_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        apitest_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        apitest_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
    except EmptyPage:
        apitest_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数# 中，则显示最后一页内容

    apitest_count = Apitest.objects.all().count()  # 统计产品数
    return render(request, "apitest_manage.html", {"user": username, "apitests":
        apitest_list, "apitestcounts": apitest_count})  # 把值赋给 apitestcounts 变量


# 搜索功能
@login_required
def apistepsearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_apiname = request.GET.get("apiname", "")
    apistep_list = Apistep.objects.filter(apiname__icontains=search_apiname)
    return render(request, 'apistep_manage.html', {"user": username, "apisteps": apistep_list})


# 搜索功能
@login_required
def apissearch(request):
    username = request.session.get('user', '')  # 读取浏览器登录 Session
    search_apiname = request.GET.get("apiname", "")
    apis_list = Apis.objects.filter(apiname__icontains=search_apiname)
    return render(request, 'apis_manage.html', {"user": username, "apiss": apis_list})


# 接口步骤管理
@login_required
def apistep_manage(request):
    username = request.session.get('user', '')
    apitestid = request.GET.get('apitest.id', None)
    apitest = Apitest.objects.get(id=apitestid)
    apistep_list = Apistep.objects.all()
    return render(request, "apistep_manage.html", {"user": username, "apitest": apitest, "apisteps": apistep_list})


# 单一接口管理
@login_required
def apis_manage(request):
    username = request.session.get('user', '')
    apis_list = Apis.objects.all()
    paginator = Paginator(apis_list, 8)  # 生成 paginator 对象，设置每页显示 8 条记录
    page = request.GET.get('page', 1)  # 获取当前的页码数，默认为第 1 页
    currentPage = int(page)  # 把获取的当前页码数转换成整数类型
    try:
        apis_list = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        apis_list = paginator.page(1)  # 如果输入的页数不是整数，则显示第 1 页内容
    except EmptyPage:
        apis_list = paginator.page(paginator.num_pages)  # 如果输入的页数不在系统的页数中，# 则显示最后一页内容
    apis_count = Apis.objects.all().count()  # 统计产品数
    return render(request, "apis_manage.html", {"user": username, "apiss": apis_list, "apiscounts":
        apis_count})  # 把值赋给 apiscounts 变量


def welcome(request):
    return render(request, "welcome.html")
