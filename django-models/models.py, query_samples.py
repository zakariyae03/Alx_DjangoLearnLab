python manage.py startapp relationship_app
INSTALLED_APPS = [
    ...
    'relationship_app',
]
from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')

    def __str__(self):
        return self.name

# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

    def __str__(self):
        return self.name
  python manage.py makemigrations relationship_app
python manage.py migrate
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: Query all books by a specific author
def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    print(f"Books by {author_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 2: List all books in a library
def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    print(f"Books in {library_name}:")
    for book in books:
        print(f"- {book.title}")

# Query 3: Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(f"Librarian for {library_name}: {librarian.name}")

# Run the queries
if __name__ == "__main__":
    # Example usage
    get_books_by_author("J.K. Rowling")
    get_books_in_library("Central Library")
    get_librarian_for_library("Central Library")
    python manage.py shell
    from relationship_app.models import Author, Book, Library, Librarian

# Create authors
author1 = Author.objects.create(name="J.K. Rowling")
author2 = Author.objects.create(name="George Orwell")

# Create books
book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)
book2 = Book.objects.create(title="1984", author=author2)

# Create libraries
library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2)

# Create librarians
librarian1 = Librarian.objects.create(name="Alice", library=library1)
python relationship_app/query_samples.py
        
        
