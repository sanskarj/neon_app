from django.shortcuts import render
from django.http import HttpResponse


def loginpage(request):
    return render(request,'neon/login.htm')
def profile(request):
    return HttpResponse('hello world')

# Create your views here.
