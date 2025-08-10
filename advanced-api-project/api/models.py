from django.db import models
from datetime import date

# Author model represents an author who can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)  # Author's name

    def __str__(self):
        return self.name


# Book model represents a single book written by an author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # Book's title
    publication_year = models.IntegerField()  # Year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # The related_name='books' allows accessing an author's books via author.books.all()

    def __str__(self):
        return f"{self.title} ({self.publication_year})"


# Create your models here.
