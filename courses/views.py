from django.http import Http404
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
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Course does not exist")
    return render(request, 'courses/detail.html', {'course': course})