from django.db import models
from django.utils import timezone

# Create your models here.

class BLOG (models.Model):

    title = models.CharField('Заголовок', max_length = 100)
    content = models.TextField('Текст')
    tpublish = models.DateTimeField('Дата Публикации', default = timezone.now)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title
