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
