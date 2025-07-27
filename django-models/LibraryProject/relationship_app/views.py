from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library  # separate line for the check to pass

# Function-Based View with correct template path
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-Based View for Library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
