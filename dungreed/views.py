from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import IO


def index(request):
    order = IO()
    order.inputs(1)
    order.inputs(1)
    return HttpResponse(order.output())

def dps_test(request):
    q = request.GET.get('공격력') # GET으로 딕셔너리 가져오고 .get으로 q키 검색해서 값 가져오는데 못가져왔을 때 None가져오라고 .get사용
    print('\n',request.GET,'\n')
    if q:
        return render(request, 'dungreed/dps.html', {'qwer':q})
    else:
        return render(request, 'dungreed/dps.html')

def test(request,reqreq):
    order = IO()
    order.inputs(reqreq)
    order_result = order.output()
    return render(request, 'dungreed/dps.html', {'order':order_result})

# https://tutorial.djangogirls.org/ko/extend_your_application/
# 에서 404 뭐시기 db에서 데이터 못찾으면 할거 그거 있음
# view에서는 처리를 해야함 (MVC의 Control)