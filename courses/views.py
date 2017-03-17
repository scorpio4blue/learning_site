from django.shortcuts import get_object_or_404, render

from .models import Course, Step


# Create your views here.

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


# pk means primary key
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def step_detail(request, course_pk, step_pk):
    step = get_object_or_404(Step, course_id=course_pk, pk=step_pk)
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