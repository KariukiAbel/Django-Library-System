from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.template import loader
from django.shortcuts import render
from django.http import Http404

# Create your views here.

def index(request):
    #To get all books in the db
    all_books = Book.objects.all()
    # html = ''
    # for book in all_books:
    #     url = '/books/' + str(book.id) + '/'
    #     html+= '<a href="'+ url +'">' + str(book.name) + '</a><br>'
    # # return HttpResponse("<h>This is the books homepage</h>")
    # return HttpResponse(html)
    # template = loader.get_template('books/index.html')
    context={
        'all_books':all_books
    }
    # return HttpResponse(template.render(context, request))
    return render(request, 'books/index.html', context)
    
    
def detail(request, book_id):
    try:
        book = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        raise Http404("This book does not exist")
    # return HttpResponse("<h2>Details for Book ID: " + str(book_id) + "</h2>")
    return render(request, 'books/detail.html', {'book':book})
