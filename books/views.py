from django.shortcuts import render,redirect, get_object_or_404
from .models import Book
from .forms import BookForm, DescriptionForm

# Create your views here.
def indexbooks(request):
    books = Book.objects.all()
    return render(request, "books/indexbooks.html", 
                  {"book": books})

def add_book(request):
    if request.method == 'GET':
        form = BookForm()
    else:
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='')

    return render(request, "books/add_book.html", {"form": form})


def add_description(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'GET':
        form = DescriptionForm()
    else:
        form = DescriptionForm(data=request.POST)
        if form.is_valid():
            new_description = form.save(commit=False)
            new_description.book = book
            new_description.save()
            return redirect(to='list_books')

    return render(request, "books/add_description.html", {
        "form": form,
        "book": book
    })


def view_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/view_book.html', {"book": book})

