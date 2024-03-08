from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name = 'index'),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('dashboard/', dashboard , name = 'dashboard'),
    path('list-books/', list_books, name='list_books'),
    path('add/', add_book, name='add_book'),
    path('edit/<int:pk>/', edit_book, name='edit_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
]