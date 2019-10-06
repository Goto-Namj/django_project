from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Calc, Item, JsonProcess
import json


def main_page(request):
    return render(request, 'dungreed/main.html',{})


def dps_test(request):
    if not request.GET:
        return render(request, 'dungreed/dps.html')
    try:
        datas=list(map(float,request.GET.dict().values()))
    except:
        return render(request, 'dungreed/dps.html', {'err':'에러'})
    q = Calc().basic(datas)
    return render(request, 'dungreed/dps.html', {'q':q})


def item_dictionary(request):
    item = Item.objects.order_by('name')
    jps = JsonProcess().lkvs(item)
    jpo = JsonProcess().lkvo(item)
    return render(request, 'dungreed/item.html',{'item':item,'jps':jps,'jpo':jpo})

# https://tutorial.djangogirls.org/ko/extend_your_application/
# 에서 404 뭐시기 db에서 데이터 못찾으면 할거 그거 있음
# view에서는 처리를 해야함 (MVC의 Control)