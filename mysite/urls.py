"""mysite URL Configuration

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
from django.urls import path
from django.http import JsonResponse
from lastest.models import User

def a(request):
    a = User()
    a.name = request.GET['name']
    a.idid = request.GET['id']
    a.passpass = request.GET['pass']

    a.save()
    print(User.objects.all())
    return JsonResponse({"TEST": True})

def b(request):
    tmp = User.objects.filter(idid=request.GET['id']).filter(passpass=request.GET['pass'])[0]
    return JsonResponse({"TEST": tmp.name})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('a/', a),
    path('b/', b),
]
