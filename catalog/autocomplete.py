from dal import autocomplete   
from .models import Book

class BookAutocomplete(autocomplete.Select2QuerySetView):
    
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Book.objects.none()

        qs = Book.objects.all()

        if self.q:
            qs = qs.filter(title__istartswith=self.q)

        return qs
    
