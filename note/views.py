from django.shortcuts import render
from django.http import HttpResponse
from .models import Note
# Create your views here.
def home(request):
    return render(request,'home.html')
def home1(request):
    return render(request,'index.html')

def validate(request):
    data = Note.objects.create(Source = request.POST['source'],
    Destination =request.POST['dest'], Amount = request.POST['amount'],
    Noon = request.POST['Noon'],Time = request.POST['time'],Date = request.POST['date'])
    data.save()
    return  HttpResponse("Done")