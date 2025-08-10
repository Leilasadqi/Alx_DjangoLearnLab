from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  # Serialize all fields of Book

    # Custom validation to ensure publication year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model with nested books
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer to include books in author representation
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
        # This will serialize author's name and a list of their books

