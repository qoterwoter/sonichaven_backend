from django.contrib import admin
from django.forms import ClearableFileInput
from django.db import models
from import_export.admin import ImportExportModelAdmin

from .models import News, NewsArticle


class NewsArticleInline(admin.TabularInline):
    list_display = ('   ')
    model = NewsArticle
    extra = 1
    formfield_overrides = {
        models.ImageField: {'widget': ClearableFileInput(attrs={'multiple': True})},
    }

@admin.register(News)
class NewsAdmin(ImportExportModelAdmin):
    list_display = ('id','title', 'created_at', 'updated_at', 'author', 'display_articles')
    list_filter = ('author',)
    search_fields = ('title',)
    inlines = [NewsArticleInline]

    def display_articles(self, obj):
        return ', '.join([article.content for article in obj.articles.all()])

    display_articles.short_description = 'Articles'
    inlines = [NewsArticleInline]

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['author'].initial = request.user.id
        return form

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user
        super().save_model(request, obj, form, change)


# @admin.register(NewsArticle)
# class NewsArticleAdmin(admin.ModelAdmin):
#     list_display = ('news', 'image_tag')
#     readonly_fields = ('image_tag',)
#     formfield_overrides = {
#         models.ImageField: {'widget': ClearableFileInput},
#     }

#     def image_tag(self, obj):
#         if obj.image:
#             return '<img src="%s" width="150px" />' % obj.image.url
#         else:
#             return '(no image)'
#     image_tag.allow_tags = True
#     image_tag.short_description = 'Image'
