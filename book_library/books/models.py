from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    name = models.CharField('Название книги', max_length=250,
                            help_text='Введите название книги')
    pub_date = models.DateTimeField('Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='books',
        verbose_name='Автор',
    )
    def __str__(self):
        return self.name[:15]

    class Meta:
        ordering = ("-pub_date",)
