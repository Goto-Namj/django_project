from django.shortcuts import render
from django.http import HttpResponse
from .models import IO

# Create your views here.
def index(request):
    order = IO()
    order.inputs(1)
    order.inputs(1)
    order.inputs(1)
    return HttpResponse(order.output())

def dps_test(request):
    return render(request, 'dungreed/dps.html', {})