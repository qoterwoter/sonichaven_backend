from django.contrib import admin
from .models import Arrangement, SoundDesigner, Service, ShopCart, CartItem, Genre
from import_export.admin import ImportExportModelAdmin
from import_export import resources

@admin.register(Arrangement)
class ArrangementAdmin(admin.ModelAdmin):
    list_display = ('genre', 'duration', 'cost', 'format', 'author')
    list_filter = ('genre', 'format', 'author')

@admin.register(SoundDesigner)
class SoundDesignerAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'nickname', 'sex', 'balance')
    list_filter = ('sex',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display = ('artist', 'sum')
    inlines = [CartItemInline]

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'cart')


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display= ('name',)
    pass


