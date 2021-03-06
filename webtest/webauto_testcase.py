#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/5/7 9:47
# software: PyCharm

# -*- coding: UTF-8 -*-
import os
import time
import unittest
import pymysql
from MainWebProject import function
from selenium import webdriver
from MainWebProject import HTMLTestRunner
from  MainWebProject import function
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
global driver
HOSTNAME = '127.0.0.1'


class Search(unittest.TestCase):
    """搜索：自动化平台测试开发，软件自动化测试开发"""

    def setUp(self):
        self.driver = webdriver.chrome()
        self.driver.get("http://www.baidu.com")
        time.sleep(1)

    def test_readSQLcase1(self):  # 流程的相关接口
        sql = "SELECT id, webfindmethod, webevelement, weboptmethod, webtestdata, webassertdata, `webtestresult` from webtest_webcasestep where webtest_webcasestep.Webcase_id = 1 ORDER BY id ASC "
        mysql=function.mysql()
        info = mysql.exe_cute(sql)
        for ii in info:
            case_list = []
        case_list.append(ii)
        webtestcase(case_list, self)
        mysql.conect_close()


def test_readSQLcase2(self):  # 流程的相关接口
    sql = "SELECT id, webfindmethod, webevelement, weboptmethod, webtestdata, webassertdata, `webtestresult` from webtest_webcasestep where webtest_webcasestep.Webcase_id = 2 ORDER BY id ASC"
    mysql=function.mysql()
    info = mysql.exe_cute(sql)
    for ii in info:
        case_list = []
    case_list.append(ii)
    webtestcase(case_list, self)
    mysql.conect_close()


def tearDown(self):
    self.driver.quit()


def webtestcase(case_list, self):
    for case in case_list:
        try:
            case_id = case[0]
            findmethod = case[1]
            evelement = case[2]
            optmethod = case[3]
            testdata = case[4]
        except Exception as e:
            return '测试用例格式不正确！%s' % e
    print(case)
    time.sleep(5)
    if optmethod == 'sendkeys' and findmethod == 'find_element_by_id':
        self.driver.find_element_by_id(evelement).send_keys(testdata)
    elif optmethod == 'click' and findmethod == 'find_element_by_name':
        print(evelement)
        self.driver.find_element_by_name(evelement).click()
    elif optmethod == 'click' and findmethod == 'find_element_by_id':
        print(evelement)
        self.driver.find_element_by_id(evelement).click()


if __name__ == '__main__':
    time.sleep(1)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Search("test_readSQLcase1"))
    testunit.addTest(Search("test_readSQLcase2"))

    filename = "../templates/webtest_report.html"
    fp = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"web 自动化测试报告", description=u"搜索测试用例")
    runner.run(testunit)
    print('Done!')
    time.sleep(1)