from django.shortcuts import render
from .models import Log
# Create your views here.
def index(request):
    users = Log.objects.all()
    context = {'users':users}
    return render(request,'logg/index.html',context)