```python
from bookshelf.models import Book

# Retrieve the book and update the title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

print(book.title)
# Output:
# Nineteen Eighty-Four
