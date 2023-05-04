from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def yutuqlar(request):
    return render(request, 'blog.html', {"yutuqlar": Yutuq.objects.all().order_by('-sana')})

def yutuq(request, pk):
    return render(request, 'yutuq.html', {"yutuq": Yutuq.objects.get(id=pk)})
