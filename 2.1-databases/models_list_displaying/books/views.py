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
        previous_object = books_object.get_previous_by_pub_date()
    except:
        previous_object = None
    try:
        next_object = books_object.get_next_by_pub_date()
    except:
        next_object = None
    context = {
        'book': books_object,
        'previous': previous_object,
        'next': next_object
    }
    return render(request, template, context)
