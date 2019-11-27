from django.shortcuts import render
from .models import Students, Courses, CourseTime
from django.views import generic
from django.db.models import Count, Q


# Create your views here.


class IndexView(generic.ListView):
    template_name = 'classschedule/index.html'

    def get_queryset(self):
        student_query = Students.objects.all()
        course_query = Courses.objects.all()
        queries = [student_query, course_query]
        return queries


class DetailView(generic.DetailView):
    model = Students
    template_name = 'classschedule/Student_detail.html'


class MasterClassView(generic.ListView):
    model = Courses
    context_object_name = 'course_list'
    template_name = 'classschedule/class_master.html'

    def get_queryset(self):
        return Courses.objects.all


class ClassListView(generic.ListView):
    model = Courses
    context_object_name = 'course_list'
    template_name = 'classschedule/classes_list.html'

    def get_queryset(self):
        student_query = Students.objects.values('enrolled_classes').annotate(num_classes=Count('enrolled_classes'))
        course_query = Courses.objects.all()
        queries = [student_query, course_query]
        return queries


class StudentListView(generic.ListView):
    model = Students
    context_object_name = 'student_list'
    template_name = 'classschedule/student_list.html'

    def get_queryset(self):
        return Students.objects.all


class SearchResultsView(generic.ListView):
    model = Students
    template_name = 'classschedule/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Students.objects.filter(Q(student_name__icontains=query))
        return object_list


class SingleClassView(generic.DetailView):
    model = Courses
    template_name = 'classschedule/Class_Detail.html'


class ChartResultsView(generic.ListView):
    template_name = 'classschedule/chartresults.html'

    def get_queryset(self):
        student_query = Students.objects.values('enrolled_classes').annotate(num_classes=Count('enrolled_classes'))
        course_query = Courses.objects.all()
        queries = [student_query, course_query]
        return queries



