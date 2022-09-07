from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.cache import cache_page

# from .forms import PostForm, CommentForm
from .models import Book
from .utils import paginate
from .forms import BookForm


def index(request):
    post_list = Book.objects.all()
    page_obj = paginate(request, post_list)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'books/index.html', context)

@login_required
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
    }
    return render(request, 'books/book_detail.html', context)

@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST or None,
                        files=request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.author = request.user
            book.save()
            return redirect('books:index')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})
