from django_filters import rest_framework as filters
# import django_filters
from todo_app.models import Todo, TodoStatus

class TodoFilter(filters.FilterSet):
    class Meta:
        model = Todo
        fields = {
            'is_completed': ['exact'],
           
        }
