from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError

from manager.models import Book


# from polls.models import Question as Poll


class Command(BaseCommand):
    help = "add simple data to database"

    def handle(self, *args, **options):
        Book.objects.all().delete()
        # User.objects.create(username='Max', password='useruser')
        # user1 = User(username='andru', password='useruser')
        # user2 = User(username='udzhin', password='useruser')
        # user3 = User(username='user123', password='useruser')
        # User.objects.bulk_create([user1, user2, user3])
        users = User.objects.all()
        book1 = Book(title='book1', text='text for book 1')
        book2 = Book(title='book2', text='text for book 2')
        book3 = Book(title='book3', text='text for book 3')
        Book.objects.bulk_create([book1, book2, book3])

        for book in Book.objects.all():
            book.authors.add(users[0], users[2])

