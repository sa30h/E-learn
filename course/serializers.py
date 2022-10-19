from rest_framework import serializers
from .models import *




class CourseSerializer(serializers.ModelSerializer):
    class Meta:
      model = course
      fields = ('id','course_name')

class CoursevisitorSerializer(serializers.ModelSerializer):
    # course_name = CourseSerializer()
    class  Meta:
          model        =           coursevisitor
          fields       =           ('id','course_name')
