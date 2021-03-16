from django.urls import path
from . import views
#from .autocomplete import  BookAutocomplete
from .models import  Book, Author, TModel
from dal import autocomplete  

class LinkedDataView(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Author.objects.all()
        book_field = self.forwarded.get('book_field',)
        author_field = self.forwarded.get('author_field',)
        if author_field:
            qs = Book.objects.all()
            qs = qs.filter(author=author_field)
            if self.q:
                qs = qs.filter(title__istartswith=self.q)
       
        return qs
       

    
urlpatterns = [
    path('', views.index, name='index'),
    path('book/', views.BookListView.as_view(), name='book'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('author/', views.AuthorListView.as_view(), name='author'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
    path('book/create/', views.BookCreate.as_view(), name='book-create'),
    path('book/<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
    path('book/<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
    path(r'linked_data/',LinkedDataView.as_view(model=TModel),name='linked_data'),
    path('search/',views.UpdateView.as_view(),name='search'),
]