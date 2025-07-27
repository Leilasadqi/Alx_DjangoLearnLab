from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    login_view,
    logout_view,
    register_view,
    admin_view,
    librarian_view,
    member_view,
    add_book,
    edit_book,
    delete_book,
)

urlpatterns = [
    # Book and library views
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication views
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    # Role-based views
    path('admin/dashboard/', admin_view, name='admin_view'),
    path('librarian/dashboard/', librarian_view, name='librarian_view'),
    path('member/dashboard/', member_view, name='member_view'),

    # Book management views (must include these literal patterns)
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book'),
]
