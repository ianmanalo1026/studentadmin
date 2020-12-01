from abc import get_cache_token

from django.db.models.query import QuerySet
from core.models import Subject, Course, Profile
from django.shortcuts import redirect, render, reverse
from core.forms import (UserRegisterForm, 
                        CourseCreationForm, 
                        SubjectCreationForm)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from core.filters import SubjectFilterForm
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView
                                  )

@login_required()
def home(request):
    return render(request, 'core/home.html')

@login_required()
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')   
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form':form}) 


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'core/loginuser.html',
                      {'form': AuthenticationForm()})
    else:
       user = authenticate(request,
                           username=request.POST['username'],
                           password=request.POST['password'])
       if user is None:
           return render(request, 'core/loginuser.html',
                         {'form': AuthenticationForm(), 
                          'error':'Username and Password did not match!'}
                         )
       else:
            login(request, user)
            return redirect('home')
        
        
@login_required()
def logoutuser(request):
    if request.method == 'GET':
        logout(request)
        return render(request, 'core/logoutuser.html')


class SubjectListView(ListView):
    model = Subject
    
    def get_context_data(self, **kwargs):
        context = super(SubjectListView, self).get_context_data(**kwargs)
        context["filter"] = SubjectFilterForm(self.request.GET, queryset=self.get_queryset())
        return context
     
    
class SubjectCreationView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ['name', 'code', 'course', 'description', 'semester', 
              'subject_year', 'school_year','start_time', 'room', 'unit'
              ]
    
    
class CourseCreationView(LoginRequiredMixin, CreateView):
    model = Course
    fields = ['name', 'code', 'description']
    success_url = 'home'
    
    
class CourseListView(ListView):
    model = Course
    ordering = ['-created_on']
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
    