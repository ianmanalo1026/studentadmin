from django.urls import path
from core import views
from core.views import SubjectCreationView, SubjectListView, CourseCreationView, CourseListView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('subject/create', SubjectCreationView.as_view(), name='create'),
    path('course/create', CourseCreationView.as_view(), name='course'),
    path('subject/', SubjectListView.as_view(), name='subject'),
    path('course/<int:pk>/', CourseListView.as_view(), name='course'),
    path('loginuser/', views.loginuser, name='loginuser'),
]