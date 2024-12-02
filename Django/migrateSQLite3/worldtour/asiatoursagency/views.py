from django.shortcuts import render
#!!
from .models import Tour
# Create your views here.
def index(request) :
    tours =  Tour.objects.all() # i want them all in this variable
    context = {'tours' : tours}
    return render(request,'tours/index.html',context) 