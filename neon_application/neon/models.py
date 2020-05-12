from django.db import models

# Create your models here.
class experience(models.Model):
    experience_title=models.CharField(max_length=200)
    experience_employment_type=models.CharField(max_length=200)
    experience_company=models.CharField(max_length=200)
    experience_location=models.CharField(max_length=200)
    experience_startmonth=models.CharField(max_length=200)
    experience_startdate=models.CharField(max_length=200)
    experience_endmonth=models.CharField(max_length=200)
    experience_enddate=models.CharField(max_length=200)
    experience_description=models.CharField(max_length=600)
    def __str__(self):
        return self.experience_title
