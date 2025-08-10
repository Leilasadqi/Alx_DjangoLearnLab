from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

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
    permission_classes = [permissions.IsAuthenticated]  # Only logged-in users

    # Optional: Automatically associate a default author if not provided
    def perform_create(self, serializer):
        # Example: automatically set a default author if missing
        # serializer.save(author=Author.objects.first())
        serializer.save()  # Normal save, you can customize as needed


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
