from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    birth_date = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "автор"
        verbose_name_plural = "авторы"
        ordering = ["last_name"]


class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    publication_date = models.DateField(verbose_name="Дата публикации")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "книга"
        verbose_name_plural = "книги"
        ordering = ["title"]


class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    loaned_at = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} - {self.user.email}"

    class Meta:
        verbose_name = "выдача книги"
        verbose_name_plural = "выдачи книг"
