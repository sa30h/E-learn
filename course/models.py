from pyexpat import model
from django.db import models

# Create your models here.
class course(models.Model):
    course_name=models.CharField( max_length=100)
    title=models.CharField( max_length=50)
    description=models.TextField()
    content=models.TextField()
    add_on=models.DateTimeField( auto_now=True)
    update_on=models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.course_name

class coursevisitor(models.Model):
    course_name=models.ForeignKey(course,on_delete=models.CASCADE)
    visit_time_on=models.TimeField(auto_now=True)
    visit_date_on=models.DateField(auto_now=True)


class coursecareer(models.Model):
    course_name=models.ForeignKey(course,on_delete=models.CASCADE)
    career_name=models.CharField( max_length=50)
    description=models.TextField()
    skill=models.CharField(max_length=50)
    salary=models.FloatField()
    jobLocation=models.CharField( max_length=100)

    