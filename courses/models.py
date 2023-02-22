from django.db import models
from django.utils import timezone

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=30)
    course_description = models.CharField(max_length=200)
    course_open_date = models.DateTimeField('date opened', default=timezone.now)

    def __str__(self):
        return self.course_title

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_no = models.IntegerField(default=0)
    session_title = models.CharField(max_length=50)
    session_objective = models.CharField(max_length=500)
    session_note = models.CharField(max_length=100)

    def __str__(self):
        return self.session_title



