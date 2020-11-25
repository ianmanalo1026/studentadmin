from django.shortcuts import render
from django.views.generic.list import ListView
from student.models import Profile


class ProfileListView(ListView):
    model = Profile
    context_object_name = 'post'
