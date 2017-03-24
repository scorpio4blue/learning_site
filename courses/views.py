from itertools import chain
from django.shortcuts import get_object_or_404, render

from . import models


# Create your views here.

def course_list(request):
    courses = models.Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# pk means primary key
def course_detail(request, pk):
    course = get_object_or_404(models.Course, pk=pk)
    steps = sorted(chain(course.text_set.all(), course.quiz_set.all()),
                   key=lambda step: step.order)
    return render(request, 'courses/course_detail.html', {
            'course': course,
            'steps': steps
        })


def text_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Text, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})


def quiz_detail(request, course_pk, step_pk):
    step = get_object_or_404(models.Quiz, course_id=course_pk, pk=step_pk)
    return render(request, 'courses/step_detail.html', {'step': step})



"""
Below is an example of the long way for a 404

from django.http import Http404

from .models import Course

def course_detail(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        raise Http404()
    else:
        return render(request, 'courses/course_detail.html', {'course': course})

"""