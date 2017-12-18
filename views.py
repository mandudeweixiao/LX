from django.shortcuts import render
from LX.models import *
# Create your views here.
def getgrades(request):
    grades=Grade.objects.all()
    context={'grades':grades}
    return render(request,'getGrades.html',context)