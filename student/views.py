from django.shortcuts import redirect, render
from django.views.generic.list import ListView
from core.models import Profile



class ProfileListView(ListView):
    model = Profile
    context_object_name = 'post'
    
    

