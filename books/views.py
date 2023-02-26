from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_objects = Book.objects.all()
    books = [element for element in books_objects]
    for element in books:
        print(element.pub_date)
    context = {'books': books}
    return render(request, template, context)

def index_html(request):
    return redirect('books')

def book_view(request, pub_date):
    books_objects = Book.objects.filter(pub_date=pub_date)
    books = [element for element in books_objects]
    template = 'books/book.html'
    context = {'filtered_books': books}
    return render(request, template, context)
