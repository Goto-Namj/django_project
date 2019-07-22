from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Calc


def dps_test(request):
    try:
        datas=list(map(float,request.GET.dict().values()))
    except:
        return render(request, 'dungreed/dps.html', {'err':'에러'})
    q = Calc().basic(datas)
    print(datas)
    return render(request, 'dungreed/dps.html', {'q':q})

# https://tutorial.djangogirls.org/ko/extend_your_application/
# 에서 404 뭐시기 db에서 데이터 못찾으면 할거 그거 있음
# view에서는 처리를 해야함 (MVC의 Control)