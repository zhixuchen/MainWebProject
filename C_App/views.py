from django.shortcuts import render
import requests,json
# Create your views here.
def post(request):
    data = '{"username":"jack","password":"123"}'
    headers = {'Content-Type': 'application/json'}
    rep = requests.post(url="http://getparameter.baozitest.top/?key=certificate", data=data, headers=headers)
    post_result_json=json.loads(rep.text)
    data={
        "post_result_json":post_result_json
    }
    return  render(request,'post.html',data)

def get(request):
    params = {
        "key":"certificate"
    }
    headers = {'Content-Type': 'application/json'}
    rep = requests.get(url="http://getparameter.baozitest.top/", params=params, headers=headers)
    get_result_json = json.loads(rep.text)
    data={
        "get_result_json":get_result_json
    }
    return  render(request,'get.html',data)



