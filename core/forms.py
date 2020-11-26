from django import forms
from django.db.models.fields import IntegerField
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import Course, Subject


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(max_length=250, required=True)
    
    class Meta:
        model = User
        fields = [
            'username', 'email', 'first_name', 'last_name', \
            'password1', 'password2'
            ]
     
        
class CourseCreationForm(ModelForm):
    
    class Meta:
        model = Course
        fields = ['name', 'code', 'description']
        

class SubjectCreationForm(ModelForm):
    
    class Meta:
        model = Subject
        fields = ['name', 'code', 'description', 'semester', 'subject_year', 'school_year','start_time', 'room', 'unit']
