from django.test import TestCase

# Create your tests here.

from MainWebProject import function

sql = "SELECT id,`apiname`,apiurl,apimethod,apiparamvalue,apiresult,`apistatus` from apitest_apistep where apitest_apistep.Apitest_id = 1 "
mysql=function.mysql()
mysql.exe_cute(sql)
mysql.conect_close()
a=mysql.result
print(a)
