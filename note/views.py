from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.utils.timezone import datetime
from .models import Note
# Create your views here.
def home(request):
    return render(request,'home.html')
def home1(request):
    data  = Note.objects.filter(Update = False)
    return render(request,'index.html',{'values':data})

def validate(request):
    data = Note.objects.create(Activity = request.GET['activity'],
    Info =request.GET['info'], Status = request.GET['status'],
    Time = datetime.now().strftime(' %H:%M:%S'),Date =datetime.now().strftime('%Y-%m-%d'))
    data.save()
    return  redirect(home1)

def additem(request):
    return render(request,'additem.html')

def update(request,value):
    data = Note.objects.get(id = value)
    data.Update = True
    data.save()
    return redirect(home1)