from django.urls import path

from . import views

app_name = 'classschedule'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='Student_detail'),
    path('class_list', views.MasterClassView.as_view(), name='class_master'),
    path('search_results', views.SearchResultsView.as_view(), name='Search_results'),
    path('student_list', views.StudentListView.as_view(), name='students_list'),
    path('classes_list', views.ClassListView.as_view(), name='class_list'),
    path('chart', views.ChartResultsView.as_view(), name='chartresults'),
    path('<int:pk>/class_detail', views.SingleClassView.as_view(), name='Class_detail'),
]