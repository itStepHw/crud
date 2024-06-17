from django.shortcuts import render, redirect

from .models import Book, Author, Genre


# Create your views here.


def index(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'library/index.html', context)


def add_author_view(request):
    authors = Author.objects.all()
    cnxt = {
        'authors': authors
    }
    return render(request, 'library/add_author.html', cnxt)


def add_author(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    bdate = request.POST['bdate']

    author = Author.objects.create(
        first_name=first_name,
        last_name=last_name,
        birth_date=bdate
    )
    return redirect('add_author_view')


def change_author_view(request, id):
    author = Author.objects.get(pk=id)
    context = {'author': author}
    return render(request, 'library/change_author.html', context)


def change_author(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    bdate = request.POST.get('bdate')
    author_id = request.POST.get('author_id')

    author = Author.objects.get(pk=author_id)
    author.first_name = first_name
    author.last_name = last_name
    author.birth_date = bdate
    author.save()
    return redirect('add_author_view')


def delete_author(request, id):
    author = Author.objects.get(pk=id)
    author.delete()
    return redirect('add_author_view')


def genre(request):
    genre = Genre.objects.all()
    context = {'genres': genre}
    return render(request, 'library/ganre.html', context)


def change_genre_view(request, id):
    genre = Genre.objects.get(pk=id)
    context = {'genre': genre}
    return render(request, 'library/change_genre.html', context)


def change_genre(request):
    name = request.POST.get('name')
    id = request.POST.get('id')
    genre = Genre.objects.get(pk=id)
    genre.name = name
    genre.save()
    return redirect('genre')


def delete_genre(request, id):
    genre = Genre.objects.get(pk=id)
    genre.delete()
    return redirect('genre')


def add_genre(request):
    name = request.POST.get('name')
    genre = Genre.objects.create(name=name)
    return redirect('genre')



def books(request):
    books = Book.objects.all()
    authors = Author.objects.all()
    genres = Genre.objects.all()
    context = {'books': books, 'authors': authors, 'genres': genres}
    return render(request, 'library/books.html', context)



def add_books(request):
    title = request.POST.get('title')
    author_id = request.POST.get('author')
    genre_ids = request.POST.getlist('genre')
    img = request.FILES.get('img')

    author_obj = Author.objects.get(id=author_id)
    genre_objs = Genre.objects.filter(id__in=genre_ids)

    book = Book.objects.create(
        title=title,
        author=author_obj,
        image=img
    )
    book.genre.set(genre_objs)

    return redirect('books')


def change_book_view(request, id):
    book = Book.objects.get(pk=id)
    author = Author.objects.all()
    genre = Genre.objects.all()
    context = {'book': book, 'authors': author, 'genres': genre}
    return render(request, 'library/change_book.html', context)



def change_book(request):
    title = request.POST.get('title')
    book_id = request.POST.get('book_id')
    author_id = request.POST.get('author')
    genre_ids = request.POST.getlist('genre')
    img = request.FILES.get('img')

    author_obj = Author.objects.get(id=author_id)
    genre_objs = Genre.objects.filter(id__in=genre_ids)
    book = Book.objects.get(pk=book_id)

    book.title = title
    book.author = author_obj
    if img:
        book.image = img

    book.save()

    book.genre.set(genre_objs)
    book.genre.set(genre_objs)
    book.save()
    return redirect('books')


def delete_book(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('books')