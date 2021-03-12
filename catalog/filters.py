import django_filters
from .models import Author, Book

class AuthorFilter(django_filters.FilterSet):
    #lname = django_filters.CharFilter(field_name='last_name', lookup_expr='icontains')
    class Meta:
        model = Author
        fields = {
            'first_name': ['icontains'],
            'last_name': ['icontains'],
        }

class BookFilter(django_filters.FilterSet):
    #title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = Book
        fields = {
            'title' : ['icontains'], 
        }