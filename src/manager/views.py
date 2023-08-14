from django.shortcuts import render
from django.urls import reverse
from django.views import View

from manager.models import Book


class BookView(View):
    def get(self, request):
        data = {'books': Book.objects.all()}
        return render(request, 'index.html', context=data)


class AddLikeView(View):
    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        book.likes += 1
        book.save()
        return reverse('list_view')