from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # import views module to use views.register explicitly

urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Use Django built-in auth views here, with template_name set
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Your registration view, named 'register' in views.py
    path('register/', views.register, name='register'),
]
from .views import admin_view, librarian_view, member_view

urlpatterns += [
    path('admin_view/', admin_view, name='admin_view'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
]
from .views import add_book, edit_book, delete_book

urlpatterns += [
    path('books/add/', add_book, name='add_book'),
    path('books/<int:pk>/edit/', edit_book, name='edit_book'),
    path('books/<int:pk>/delete/', delete_book, name='delete_book'),
]
