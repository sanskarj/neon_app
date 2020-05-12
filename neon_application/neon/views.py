from django.shortcuts import render
from django.http import HttpResponse
from .models import experience
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def experience_form(request):
    print("form_submitted")
    try:
        experience_title=request.POST["experience_title"]
    except MultiValueDictKeyError:
        experience_title=False
    try:
        experience_employment_type=request.POST["experience_employment_type"]
    except MultiValueDictKeyError:
        experience_employment_type=False
    try:
        experience_company=request.POST["experience_company"]
    except MultiValueDictKeyError:
        experience_company=False
    try:
        experience_location=request.POST["experience_location"]
    except MultiValueDictKeyError:
        experience_location=False
    try:
        experience_startmonth=request.POST["experience_startmonth"]
    except MultiValueDictKeyError:
        experience_startmonth=False
    try:
        experience_startdate=request.POST["experience_startdate"]
    except MultiValueDictKeyError:
        experience_startdate=False
    try:
        experience_endmonth=request.POST["experience_endmonth"]
    except MultiValueDictKeyError:
        experience_endmonth=False
    try:
        experience_enddate=request.POST["experience_enddate"]
    except MultiValueDictKeyError:
        experience_enddate=False
    try:
        experience_description=request.POST["experience_description"]
    except MultiValueDictKeyError:
        experience_description=False
    experiencey=experience(experience_title=experience_title,experience_employment_type=experience_employment_type,experience_company=experience_company,experience_location=experience_location,experience_startmonth=experience_startmonth,experience_startdate=experience_startdate, experience_endmonth=experience_endmonth,experience_enddate=experience_enddate,experience_description=experience_description)
        # experiencey=experience(experience_title=experience_title,experience_employment_type=experience_employment_type,experience_company=experience_company,experience_location=experience_location,experience_description=experience_description)

    experiencey.save()
    return render(request,'x.html')