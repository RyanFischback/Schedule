from django.db import models

# Create your models here.


class CourseTime(models.Model):
    course_time = models.CharField(max_length=50)

    class Meta:
        ordering = ('course_time',)

    def __str__(self):
        return self.course_time


class Courses(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200)
    Time = models.ManyToManyField(CourseTime)

    class Meta:
        ordering = ('course_name',)

    def __str__(self):
        return self.course_name


class Students(models.Model):
    student_name = models.CharField(max_length=50)
    student_address = models.CharField(max_length=200)
    student_phonenumber = models.CharField(max_length=200)
    enrolled_classes = models.ManyToManyField(Courses)

    def __str__(self):
        return self.student_name
