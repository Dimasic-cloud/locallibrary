from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'is_available', 'added_date')
    list_filter = ('genre', 'is_available', 'added_date')
    search_fields = ('title', 'author', 'description')
    readonly_fields = ('added_date',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'author', 'isbn', 'genre')
        }),
        ('Описание', {
            'fields': ('description', 'pages'),
            'classes': ('collapse',)
        }),
        ('Статус', {
            'fields': ('is_available', 'added_date')
        }),
    )