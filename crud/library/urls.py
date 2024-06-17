from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('add_author_view', add_author_view, name='add_author_view'),
    path('add_author', add_author, name='add_author'),
    path('change_author_view/<int:id>', change_author_view, name='change_author_view'),
    path('change_author', change_author, name='change_author'),
    path('delete_author/<int:id>', delete_author, name='delete_author'),

    path('genre', genre, name='genre'),
    path('add_genre', add_genre, name='add_genre'),
    path('change_genre_view/<int:id>', change_genre_view, name='change_genre_view'),
    path('change_genre', change_genre, name='change_genre'),
    path('delete_genre/<int:id>', delete_genre, name='delete_genre'),

    path('books', books, name='books'),
    path('add_books', add_books, name='add_books'),
    path('change_book_view/<int:id>', change_book_view, name='change_book_view'),
    path('change_book', change_book, name='change_book'),
    path('delete_book/<int:id>', delete_book, name='delete_book'),

]