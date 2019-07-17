from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import IO


def index(request):
    order = IO()
    order.inputs(1)
    order.inputs(1)
    order.inputs(1)
    return HttpResponse(order.output())

def dps_test(request,reqreq):
    order = IO()
    order.inputs(reqreq)
    order_result = order.output()
    return render(request, 'dungreed/dps.html', {'order':order_result})

# https://tutorial.djangogirls.org/ko/extend_your_application/
# 에서 404 뭐시기 db에서 데이터 못찾으면 할거 그거 있음
# view에서는 처리를 해야함 (MVC의 Control)