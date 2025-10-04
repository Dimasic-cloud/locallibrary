from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Название книги"
    )

    author = models.CharField(
        max_length=100,
        verbose_name="Автор"
    )

    isbn = models.CharField(
        max_length=13,
        verbose_name="isbn",
        help_text="13 символов <a href=https://www.isbn-international.org/content/what-isbn'>ISBN номер</a>"
    )

    genre = models.CharField(
        max_length=50,
        verbose_name="Жанр",
        choices=[
            ('fiction', 'Художественная литература'),
            ('science', 'Научная литература'),
            ('fantasy', 'Фэнтези'),
            ('detective', 'Детектив'),
            ('biography', 'Биография'),
        ],
        default='fiction'
    )

    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        help_text='Краткое описание книги'
    )

    added_date = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата поступления"
    )

    is_available = models.BooleanField(
        default=True,
        verbose_name="Доступна для выдачи"
    )

    pages = models.IntegerField(
        verbose_name='Количество строниц',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"{self.title} - {self.auth}"