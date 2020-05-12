from django.shortcuts import render
from django.http import HttpResponse
from .models import SkillInfo


def loginpage(request):
    return render(request,'neon/login.htm')
def profile(request):
    all_skills=SkillInfo.objects.all()
    return render(request,'neon/profile.htm',{'Skills':all_skills})

def AddSkill(request):
    return render(request, 'neon/add_skill.htm')

def add_skill_form_submit(request):
    skill_name=request.POST["skill_name"]
    skill_score=request.POST["skill_score"]
    
    skill_info=SkillInfo(skill_name=skill_name,skill_score=skill_score)
    
    skill_info.save()
    print(skill_info.skill_name)
    print(skill_info.skill_score)
    return render(request,'neon/profile.htm')

