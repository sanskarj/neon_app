from django.shortcuts import render
from django.http import HttpResponse


def loginpage(request):
    return render(request,'neon/login.htm')
def profile(request):
    return render(request,'neon/profile.htm')

# Create your views here.
