from unicodedata import category
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Category
from .forms import BookForm

# Create your views here.
def indexbooks(request):
    books = Book.objects.all()
    return render(request, "books/indexbooks.html", 
                  {"books": books})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='indexbooks')

    return render(request, "books/add_book.html", {"form": form})


def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/view_book.html', 
                    {"book": book})

def books_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    books = Book.objects.filter(category=category)
    return render(request, 'books/category.html',  {"books": books})


