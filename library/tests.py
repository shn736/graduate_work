from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from library.models import Author, Book, BookLoan
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@sky.pro")
        self.author = Author.objects.create(
            first_name="Александр", last_name="Пушкин", birth_date="1799-05-26"
        )
        self.book = Book.objects.create(
            title="Руслан и Людмила", publication_date="2000-05-26", author=self.author
        )
        self.client.force_authenticate(user=self.user)

    def test_author_retrieve(self):
        url = reverse("library:author-detail", args=(self.author.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("first_name"), self.author.first_name)

    def test_book_retrieve(self):
        url = reverse("library:books-detail", args=(self.book.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), self.book.title)

    def test_author_create(self):
        url = reverse("library:author-create")
        data = {
            "first_name": "Лев",
            "last_name": "Толстой",
            "birth_date": "1828-08-28",
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.all().count(), 2)

    def test_book_create(self):
        url = reverse("library:books-list")
        data = {
            "title": "Война и мир",
            "publication_date": "2000-05-26",
            "author": self.author.pk,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.all().count(), 2)

    def test_author_update(self):
        url = reverse("library:author-update", args=(self.author.pk,))
        data = {"first_name": "Алексей"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("first_name"), "Алексей")

    def test_book_update(self):
        url = reverse("library:books-detail", args=(self.book.pk,))
        data = {"title": "Буратино"}
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("title"), "Буратино")

    def test_author_delete(self):
        url = reverse("library:author-delete", args=(self.author.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Author.objects.all().count(), 0)

    def test_book_delete(self):
        url = reverse("library:books-detail", args=(self.book.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.all().count(), 0)

    def test_author_list(self):
        url = reverse("library:author-list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = [
            {
                "id": 4,
                "first_name": "Александр",
                "last_name": "Пушкин",
                "birth_date": "1799-05-26",
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)

    def test_book_list(self):
        url = reverse("library:books-list")
        response = self.client.get(url)
        data = response.json()
        print(data)
        result = [
            {
                "id": 9,
                "title": "Руслан и Людмила",
                "publication_date": "2000-05-26",
                "author": 9,
            }
        ]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
