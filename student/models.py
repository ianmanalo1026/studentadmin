from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    school_year = models.SmallIntegerField(blank=True)
    start_time = models.TimeField()
    room = models.CharField(max_length=50)
    unit = models.SmallIntegerField(blank=True)
    prelim = models.SmallIntegerField(blank=True)
    midterm = models.SmallIntegerField(blank=True)
    finals = models.SmallIntegerField(blank=True)
    
    def __str__(self):
        return self.name

class Profile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, \
                                   blank=True, null=True)
    course = models.OneToOneField('Course', on_delete=models.CASCADE, null=True)
    subject = models.ManyToManyField('Subject')
    
    def __str__(self):
        return str(self.student)