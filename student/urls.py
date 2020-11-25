from django.urls import path
from student.views import ProfileListView


urlpatterns = [
    path('', ProfileListView.as_view(), name='student-list')
]