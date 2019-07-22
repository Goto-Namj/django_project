from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Calc


def dps_test(request):
    check_list = ['1','2','3','4','5','6','7']
    for i in check_list:
        if not request.GET.get(i):
            return render(request, 'dungreed/dps.html')
    datas=list(map(float,request.GET.dict().values()))
    q = Calc().basic(datas)
    print(datas)
    return render(request, 'dungreed/dps.html', {'q':q})

# https://tutorial.djangogirls.org/ko/extend_your_application/
# 에서 404 뭐시기 db에서 데이터 못찾으면 할거 그거 있음
# view에서는 처리를 해야함 (MVC의 Control)