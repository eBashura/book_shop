from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from django.db.models import Count

from manager.models import Book


# from polls.models import Question as Poll


class Command(BaseCommand):

    def handle(self, *args, **options):
        books = Book.objects.annotate(likes_book=Count('likes'))
        for book in books:
            book.count_likes = book.likes_book
        Book.objects.bulk_update(books, ['count_likes'])
        book.save()
