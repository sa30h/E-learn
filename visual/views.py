import imp
from django.shortcuts import render
from course.models import *
from django.db.models import Count

# Create your views here.

def graph(request):
    context={}
    data=coursevisitor.objects.values('course_name').annotate(visitorcount=Count('course_name')).order_by()
    coursename=course.objects.all().values('id','course_name')

    datadict={}
    for i in coursename:
        for j in data:
            if(i['id']==j['course_name']):
                datadict[i['course_name']]=j['visitorcount']

    courselabellist=list(datadict.keys())
    visitorcountlist=list(datadict.values())
    context['courselabellist']=courselabellist
    context['visitorcountlist']=visitorcountlist
    
    return render(request,'visual/graph.html',context)