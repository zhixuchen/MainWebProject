from django.shortcuts import render
import pymysql,os,configparser,json
# Create your views here
from MainWebProject.function import *
def apilist(request):
    url=get_config('url','get_api_list')
    header={}
    params={
        "projectID":1
    }
    api_list=get(url,header,params)

    url = get_config('url', 'get_env_list')
    header = {}
    params = {
        "projectID": 1
    }
    env_list = get(url, header, params)
    data={
        "api_list":api_list,
        "env_list":env_list
    }


    return render(request,"TestCenter.html",data)

def apidel(request):
    url=get_config('url','get_api_del')
    header={}
    apiID=request.GET['apiID']
    envID=request.GET['envID']
    params={
        "apiID":apiID,
        "envID":envID
    }
    apidel=get(url,header,params)
    url=get_config('url','get_api_result')
    apiresult=get(url,header,params)

    url=get_config('url','get_env_del')
    envdel=get(url,header,params)
    result={}
    result["apidel"]=apidel
    result["apiresult"] = apiresult
    result["envdel"] = envdel
    return render(request,"apidel.html",result)






# if __name__ == '__main__':
#     apidel(11)