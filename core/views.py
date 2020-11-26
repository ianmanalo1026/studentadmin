from core.models import Subject
from django.shortcuts import redirect, render, reverse
from core.forms import (UserRegisterForm, 
                        CourseCreationForm, 
                        SubjectCreationForm)
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.views.generic import (
                                  ListView,
                                  DetailView,
                                  CreateView,
                                  DeleteView
                                  )


def home(request):
    return render(request, 'core/home.html')

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
        return render(request, 'core/loginuser.html', {'form': AuthenticationForm()})
    else:
       user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
       if user is None:
           return render(request, 'core/loginuser.html', {'form': AuthenticationForm(), 'error':'Username and Password did not match!'})
       else:
            login(request, user)
            return redirect('home')
        

def course(request):
    if request.method == 'POST':
        u_form = CourseCreationForm()
        if u_form.is_valid():
            u_form.save()
            name = u_form.cleaned_data.get()
            return redirect('home')
    else:
        u_form = CourseCreationForm()
    return render(request, 'core/course.html', {'form': u_form})


def subject(request):
    if request.method == 'POST':
        u_form = SubjectCreationForm()
        if u_form.is_valid():
            u_form.save()
            name = u_form.cleaned_data.get()
            return redirect('home')
    else:
        u_form = SubjectCreationForm()
    return render(request, 'core/subject.html', {'form': u_form})


class SubjectCreationView(LoginRequiredMixin, CreateView):
    model = Subject
    fields = ['name', 'code', 'description', 'semester', 'subject_year', 'school_year','start_time', 'room', 'unit']
    
    def form_valid(self, form):
        form.instance.user.profile.status = self.request.user.profile.status
        return super().form_valid()
    