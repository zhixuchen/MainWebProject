#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:zxchen
# datetime:2019/4/16 11:13
# software: PyCharm
import pymysql,os,configparser,requests,json
def mysqlconect(sql):  ##数据库操作
    try:
        # 打开数据库连接
        # db = pymysql.connect("47.96.87.38", "chenzx", "123456", "eolinker_os");
        db_host = get_config("db", "db_host")
        # db_port = get_config("db", "db_port")
        db_name = get_config("db", "db_name")
        db_user = get_config("db", "db_user")
        db_pass = get_config("db", "db_pass")
        db = pymysql.connect(db_host, db_user, db_pass, db_name);

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # 使用execute方法执行SQL语句
        a = cursor.execute(sql)
        if sql.find("SELECT") >= 0:
            results = cursor.fetchall()
        else:
            results = a
        db.commit()
        # 关闭数据库连接
        db.close()
        return results
    except:
        # 如果发生错误则回滚
        db.rollback()


def get_config(title,key):
    root_path=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))#项目路径
    ini_path=root_path+"/TestCenter.ini"
    config = configparser.ConfigParser()
    config.read(ini_path,encoding='utf-8')
    result = config.get(title, key)
    return result


def post(url,header,data):
    headers = header
    rep = requests.post(url=url, data=data, headers=headers)
    post_result_json=json.loads(rep.text)
    result=post_result_json
    return result

def get(url,header,params):

    headers = header
    rep = requests.get(url=url, params=params, headers=headers)
    get_result_json = json.loads(rep.text)
    result=get_result_json
    return result