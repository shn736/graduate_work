from rest_framework import serializers

from library.models import Author, Book, BookLoan


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookLoan
        fields = "__all__"
