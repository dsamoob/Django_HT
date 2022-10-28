from django.shortcuts import render, get_object_or_404
from books.models import Book


def first_page(request):
    template = 'books/first_page.html'
    return render(request, template)


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.order_by('pub_date').all()

    return render(request, template, {'books': books_objects})


def book(request, pub_date):
    template = 'books/one_book.html'
    books_object = get_object_or_404(Book, pub_date=pub_date)
    try:
        previous_book = Book.objects.order_by('pub_date').filter(pub_date__lt=books_object.pub_date).first()
    except:
        previous_book = None
    try:
        next_book = Book.objects.order_by('pub_date').filter(pub_date__gt=books_object.pub_date).first()
    except:
        next_book = None
    context = {
        'book': books_object,
        'previous': previous_book,
        'next': next_book
    }
    return render(request, template, context)
