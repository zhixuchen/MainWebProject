from django.shortcuts import render

# Create your views here.
def login(request):
    if request.method=="POST":
        account = request.POST.get('username')
        pwd = request.POST.get('password')
        print(account)
        print(pwd)
    return render(request,'login.html')