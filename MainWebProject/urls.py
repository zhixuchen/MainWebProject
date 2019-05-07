"""MainWebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from center import views
from product import proviews
from apitest import apitestviews
from bug import bugviews
from set import setviews
from apptest import apptestviews
from webtest import webtestviews
from report import reportviews

urlpatterns = [
    path('',views.index),
    path('A', include("A_App.urls")),
    path('B', include("B_App.urls")),
    path('C/', include("C_App.urls")),
    path('D', include("D_App.urls")),
    path('T', include("T_App.urls")),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('home/', views.home),
    path('logout/', views.logout),
    path('product_manage/', proviews.product_manage),
    path('apitest_manage/', apitestviews.apitest_manage),
    path('apistep_manage/', apitestviews.apistep_manage),
    path('apis_manage/', apitestviews.apis_manage),
    path('bug_manage/', bugviews.bug_manage),
    path('bugsearch/', bugviews.bugsearch),
    path('set_manage/', setviews.set_manage),
    path('user/', setviews.set_user),
    path('appcase_manage/', apptestviews.appcase_manage),
    path('appcasestep_manage/', apptestviews.appcasestep_manage),
    path('webcase_manage/', webtestviews.webcase_manage),
    path('webcasestep_manage/', webtestviews.webcasestep_manage),
    path ('test_report/', apitestviews.test_report),
    path('left/', views.left),
    path ('apisearch/', apitestviews.apisearch),
    path ('setsearch/', setviews.setsearch),
    path ('productsearch/', proviews.productsearch),
    path ('apissearch/', apitestviews.apissearch),
    path ('bugsearch/', bugviews.bugsearch),
    path('appsearch/', apptestviews.appsearch),
    path('appstepseach/', apptestviews.appstepsearch),
    path('websearch/', webtestviews.websearch),
    path('webstepsearch/', webtestviews.webstepsearch),
    path ('usersearch/', setviews.usersearch),
    path('productsearch/', proviews.productsearch),
    path('apistepsearch/', apitestviews.apistepsearch),
    path ('welcome/', apitestviews.welcome),
    path('apistep_manage/', apitestviews.apistep_manage,name='apistep_manage'),
    path('appcasestep_manage/', apptestviews.appcasestep_manage,name='appcasestep_manage'),
    path('webcasestep_manage/', webtestviews.webcasestep_manage,name='webcasestep_manage'),
    path('apitest_report/',reportviews.apitest_report),
    path('apisteptest_report/',reportviews.apisteptest_report),
]
