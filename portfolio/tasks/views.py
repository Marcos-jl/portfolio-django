from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'tasks/index.html')
