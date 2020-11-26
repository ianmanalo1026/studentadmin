from django.urls import path
from core import views
from core.views import SubjectCreationView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('course/', views.course, name='course'),
    path('subject/', views.subject, name='subject'),
    path('subject2/', SubjectCreationView.as_view(), name='subject2'),
    path('loginuser/', views.loginuser, name='loginuser'),
]