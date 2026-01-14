from rest_framework import permissions
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Author, Book, BookLoan
from .serializers import AuthorSerializer, BookLoanSerializer, BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorCreateApiView(CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorListApiView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorRetrieveApiView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorUpdateApiView(UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class AuthorDestroyApiView(DestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class BookViewSet(ModelViewSet):
    """Создаем фильтр: возвращаем все книги, которые не запрашиваются и выданы данному пользователю"""

    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queried_books = BookLoan.objects.filter(user=user).values_list(
            "book_id", flat=True
        )
        return Book.objects.exclude(id__in=queried_books)


class BookLoanViewSet(ModelViewSet):
    queryset = BookLoan.objects.all()
    serializer_class = BookLoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Возвращаем только те записи о выдаче, которые выданы текущему пользователю"""
        user = self.request.user
        return BookLoan.objects.filter(user=user)
