from django.contrib import admin

# Register your models here.

from .models import BLOG

class ModelAdmin (admin.ModelAdmin):
    # Никаких методов здесь, только свойства = поля
    list_display = ['title', 'tpublish'] # Поля, которые мы хотим отображать в админской части
    list_display_links = ['title'] # Поля, на которые мы хотим повесить ссылки
    list_filter = ['tpublish'] # Поля, по которым мы хотим сделать фильтрацию
    search_fields = ['title', 'content'] # Поля, по которым будет поиск
    list_editable = ['tpublish'] # Поля, которые можно будет изменить в режиме "экспресс"

admin.site.register(BLOG, ModelAdmin)
