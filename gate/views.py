from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.
def home_page(request):
    data = Question.objects.all()
    value = { i.Gate for i in data}
    return render(request,'gate.html',{"data":value})