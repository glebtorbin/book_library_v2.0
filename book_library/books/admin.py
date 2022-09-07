from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'pub_date', 'author',)
    search_fields = ('name',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Book, BookAdmin)
