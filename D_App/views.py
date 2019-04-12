from django.shortcuts import render
import configparser ,os
# Create your views here.
def config(request):
    db_host = get_config("db", "db_host")
    db_port = get_config("db", "db_port")
    db_name = get_config("db", "db_name")
    db_user = get_config("db", "db_user")
    db_pass = get_config("db", "db_pass")
    data={
        "db_host":db_host,
        "db_port":db_port,
        "db_name":db_name,
        "db_user":db_user,
        "db_pass":db_pass
    }
    return render(request,'index.html',data)

def get_config(title,key):
    root_path=os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))#项目路径
    print(root_path)
    ini_path=root_path+"/D.ini"
    config = configparser.ConfigParser()
    config.read(ini_path,encoding='utf-8')
    result = config.get(title, key)
    return result



