from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Course

def index(request):
    latest_course_list = Course.objects.order_by('-course_open_date')[:10]
    context = {
        'latest_course_list': latest_course_list,
    }
    return render(request, 'courses/index.html', context)

def detail(request, course_id):
    return HttpResponse("You are looking at course %s." % course_id)