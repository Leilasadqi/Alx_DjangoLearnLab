from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering.

    Filtering: Filter by 'title', 'author' (by author id), and 'publication_year'.
    Searching: Search by 'title' and author's 'name'.
    Ordering: Order by 'title' and 'publication_year'.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['title', 'publication_year', 'author']

    search_fields = ['title', 'author__name']

    ordering_fields = ['title', 'publication_year']


# --------------------------
# BOOK GENERIC VIEWS
# --------------------------

# List all books (read-only, open to everyone)
class BookListView(generics.ListAPIView):
    """
    List all books in the database.
    Accessible to all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Read access for everyone


# Retrieve one book by ID (read-only, open to everyone)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by its ID.
    Accessible to all users (authenticated or not).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book instance.
    Only authenticated users can create books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Optional: Automatically associate a default author if not provided
    def perform_create(self, serializer):
        serializer.save()


# Update an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book.
    Only authenticated users can update books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete an existing book.
    Only authenticated users can delete books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
