from django.urls import path

from . import views
urlpatterns = [
    path('',views.profile,name="profile"),
    path('add_skill/',views.AddSkill,name="add_skill"),
    path('add_skill_form_submit/',views.add_skill_form_submit,name="add_skill_form_submit")
   
    
]
