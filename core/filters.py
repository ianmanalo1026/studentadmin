import django_filters
from core.models import Subject


class SubjectFilterForm(django_filters.FilterSet):
    
    class Meta:
        model = Subject
        fields = {
            'code': ['icontains'],
            }