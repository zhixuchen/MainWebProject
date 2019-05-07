#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/5/6 9:23
# software: PyCharm
from apitest.report import *
from MainWebProject import HTMLTestRunner
import time
# import unittest


if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # testunit = unittest.TestSuite()
    # testunit.addTest(ApiFlow("test_readSQLcase"))
    test(1)
    # filename = "../templates/apitest_report.html"
    # print(filename)
    # fp = open(filename, 'wb')
    # runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"单一接口测试报告", description=u"单一接口")
    # runner.run(testunit)

    # readSQLcase()
    print('Done!')
    time.sleep(1)
