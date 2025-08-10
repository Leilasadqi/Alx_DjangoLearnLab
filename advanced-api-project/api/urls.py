from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView
)

urlpatterns = [
    # GET: list all books
    path('books/', BookListView.as_view(), name='book-list'),

    # POST: create a new book
    path('books/create/', BookCreateView.as_view(), name='book-create'),

    # GET: retrieve a book
    # PUT/PATCH: update a book
    # DELETE: delete a book
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),   # Read only
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),  # Update
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),  # Delete
]
