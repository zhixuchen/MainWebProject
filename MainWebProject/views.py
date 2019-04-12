from django.shortcuts import render
import pymysql

# Create your views here.
def index(request):
    return render(request, 'index.html')




