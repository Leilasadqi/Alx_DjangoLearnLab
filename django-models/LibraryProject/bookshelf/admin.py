from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to show
    list_filter = ('publication_year',)                     # Filter sidebar
    search_fields = ('title', 'author')                     # Search box

# Alternatively, without decorator:
# admin.site.register(Book, BookAdmin)
