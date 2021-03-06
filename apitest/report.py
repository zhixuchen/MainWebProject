#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/5/7 11:32
# software: PyCharm

import json
import re
import time
import unittest
import urllib  # ,

import pymysql
import requests
from MainWebProject import function



# import fconfig

HOSTNAME = '127.0.0.1'



def test(test_id):
    sql = "SELECT id,`apiname`,apiurl,apimethod,apiparamvalue,apiresult ,`apistatus` FROM apitest_apis where apitest_apis.id="+str(test_id)+"; "
    mysql = function.mysql()
    mysql.exe_cute(sql)
    info=mysql.result
    for ii in info:
        case_list = []
        case_list.append(ii)
    # CredentialId()
    interfaceTest(case_list)
    mysql.conect_close()


def interfaceTest(case_list):
    res_flags = []
    request_urls = []
    responses = []
    strinfo = re.compile('{TaskId}')
    strinfo1 = re.compile('{AssetId}')
    strinfo2 = re.compile('{PointId}')
    assetinfo = re.compile('{assetno}')
    tasknoinfo = re.compile('{taskno}')
    schemainfo = re.compile('{schema}')

    for case in case_list:
        try:
            case_id = case[0]
            interface_name = case[1]
            method = case[3]
            url = case[2]
            param = case[4]
            res_check = case[5]
        except Exception as e:
            return '测试用例格式不正确！%s' % e

        url = strinfo.sub(TaskId, url)
        param = strinfo.sub(TaskId, param)
        param = tasknoinfo.sub(taskno, param)
        new_url = 'http://' + url
        request_urls.append(new_url)
        if method.upper() == 'GET':
            headers = {'Authorization': '', 'Content-Type': 'application/json'}
            if "=" in urlParam(param):
                data = None
                results = requests.get(new_url + '?' + urlParam(param), data, headers=headers).text
                responses.append(results)
                res = readRes(results, res_check)
            if 'pass' == res:
                res_flags.append('pass')
                writeResult(case_id, '1')
                # caseWriteResult(case_id, '1')
            else:
                res_flags.append('fail')
                writeResult(case_id, '0')
                # caseWriteResult(case_id, '0')
        if method.upper() == 'PUT':
            headers = {'Host': HOSTNAME, 'Connection': 'keep-alive', 'CredentialId': id,
                       'Content-Type': 'application/json'}
            body_data = param
            results = requests.put(url=url, data=body_data, headers=headers)
            responses.append(results)
            res = readRes(results, res_check)
            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)
            try:
                preOrderSN(results)
            except:
                print('ok')
        if method.upper() == "PATCH":
            headers = {'Authorization': 'Credential ' + id, 'Content-Type': 'application/json'}
            data = None
            results = requests.patch(new_url + '?' + urlParam(param), data, headers=headers).text
            responses.append(results)
            res = readRes(results, res_check)
            if 'pass' == res:
                writeResult(case_id, 'pass')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, 'fail')
                writeBug(case_id, interface_name, new_url, results, res_check)
            try:
                preOrderSN(results)
            except:
                print('ok')
        if method.upper() == "POST":
            headers = {'Authorization': 'Credential ' + id, 'Content-Type': 'application/json'}
            if "=" in urlParam(param):
                data = None
                results = requests.patch(new_url + '?' + urlParam(param), data, headers=headers).text
                print(' response is post' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, '')
            else:
                print(str(case_id) + ' request is ' + new_url.encode('utf-8') + ' body is ' + urlParam(param).encode(
                    'utf - 8'))
                results = requests.post(new_url, data=urlParam(param).encode('utf-8 '), headers=headers).text
                print(' response is post' + results.encode('utf-8'))
                responses.append(results)
                res = readRes(results, res_check)
            if 'pass' == res:
                writeResult(case_id, '1')
                res_flags.append('pass')
            else:
                res_flags.append('fail')
                writeResult(case_id, '0')
                writeBug(case_id, interface_name, new_url, results, res_check)
            try:
                TaskId(results)
            except:
                print('ok1')


def readRes(res, res_check):
    res_check = res_check.split(';')
    for s in res_check:
        if s in res:
            pass
        else:
            return '错误，返回参数和预期结果不一致' + s
    return 'pass'


def urlParam(param):
    param1 = param.replace('&quot;', '"')
    return param1


def CredentialId():
    global id
    url = 'http://' + 'api.test.com.cn' + '/api/Security/Authentication/Signin/web'
    body_data = json.dumps({"Identity": 'test', "Password": 'test'})
    headers = {'Connection': 'keep-alive', 'Content-Type': 'application/json'}
    response = requests.post(url=url, data=body_data, headers=headers)
    data = response.text
    regx = '.*"CredentialId":"(.*)","Scene"'
    pm = re.search(regx, data)
    id = pm.group(1)


def preOrderSN(results):
    global preOrderSN
    regx = '.*"preOrderSN":"(.*)","toHome"'
    pm = re.search(regx, results)
    if pm:
        preOrderSN = pm.group(1).encode('utf-8')
    return preOrderSN
    return False


def TaskId(results):
    global TaskId
    regx = '.*"TaskId":(.*),"PlanId"'
    pm = re.search(regx, results)
    if pm:
        TaskId = pm.group(1).encode('utf-8')
    return TaskId
    return False


def taskno(param):
    global taskno
    a = int(time.time())
    taskno = 'task_' + str(a)
    return taskno


def writeResult(case_id, result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apitest_apis set apitest_apis.apistatus=%s,apitest_apis.create_time=%s where apitest_apis.id = %s;"
    param = (result, now, case_id)
    print('api autotest result is ' + result.decode())
    mysql = function.mysql()
    mysql.exe_cute(sql,param)
    mysql.conect_close()


def caseWriteResult(case_id, result):
    result = result.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE apitest_apitest set apitest_apitest.apitestresult=%s,apitest_apitest.create_time=%s where apitest_apitest.id = % s; "
    param = (result, now, case_id)
    print('api autotest result is ' + result.decode())
    mysql = function.mysql()
    mysql.exe_cute(sql, param)
    mysql.conect_close()


def writeBug(bug_id, interface_name, request, response, res_check):
    interface_name = interface_name.encode('utf-8')
    res_check = res_check.encode('utf-8')
    request = request.encode('utf-8')
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    bugname = str(bug_id) + '_' + interface_name.decode() + '_出错了'
    bugdetail = '[请求数据]<br />' + request.decode() + '<br/>' + '[预期结果] < br / > ' + res_check.decode() + ' < br / > ' + ' < br / > ' + '[响应数据] < br / > ' + ' < br / > ' + response.decode()
    print(bugdetail)
    sql = "INSERT INTO `bug_bug` (`bugname`,`bugdetail`,`bugstatus`,`buglevel`, `bugcreater`,`bugassign`, `created_time`, `Product_id`) VALUES ('%s', '%s', '1', '1', '邹辉', '邹辉', '%s','2');" % (
        bugname, pymysql.escape_string(bugdetail), now)
    mysql = function.mysql()
    mysql.exe_cute(sql)
    mysql.conect_close()