from django.shortcuts import render
from .models import Log
from django.http import JsonResponse
import json
# Create your views here.
def index(request):
    users = Log.objects.all()
    context = {'users':users}
    return render(request,'logg/index.html',context)
def json(requset):
    data =  list(Log.objects.values())
    return JsonResponse(data,safe=False)