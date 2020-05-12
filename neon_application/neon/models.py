from django.db import models

class SkillInfo(models.Model):
    skill_name=models.CharField(max_length=200)
    skill_score=models.CharField(max_length=2)
    
    
    def __str__(self):
        return self.skill_name