from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Course(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=20)
    description = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Subject(models.Model):
    
    SEMESTER_CHOICES = (
        ('1st', 'First'),
        ('2nd', 'Second'),
        ('3rd', 'Third')
    )

    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=50, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    school_year = models.PositiveIntegerField()
    semester = models.CharField(max_length=50, choices=SEMESTER_CHOICES)
    subject_year = models.CharField(max_length=50, choices=SEMESTER_CHOICES)
    start_time = models.TimeField()
    room = models.CharField(max_length=50)
    unit = models.SmallIntegerField(blank=True, null=True)
    prelim = models.SmallIntegerField(blank=True, null=True)
    midterm = models.SmallIntegerField(blank=True, null=True)
    finals = models.SmallIntegerField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name)
    

class Profile(models.Model):
    
    STATUS_CHOICES = (
        ('Student', 'Student'),
        ('Graduate', 'Graduate'),
        ('Professor', 'Professor'),
    )

    student = models.OneToOneField(User, on_delete=models.CASCADE, \
                                   blank=True, null=True)
    course = models.OneToOneField('Course', on_delete=models.CASCADE, null=True)
    subject = models.ManyToManyField('Subject')
    created_on = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to=None)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    
    def __str__(self):
        return str(self.student)
    
    
