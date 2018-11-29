from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World!")

def resume(request):
    return render(request, 'resume.html')