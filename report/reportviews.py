from django.shortcuts import render

# Create your views here.
def apitest_report(request):
    return render(request, 'apitest_report.html')

def apisteptest_report(request):
    return render(request, 'apisteptest_report.html')


