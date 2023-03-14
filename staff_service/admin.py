from django.contrib import admin
from .models import Arrangement, SoundDesigner, Service, ShopCart, CartItem, Genre
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.html import format_html_join

@admin.register(Arrangement)
class ArrangementAdmin(admin.ModelAdmin):
    list_display = ('genre', 'duration', 'cost', 'format', 'author')
    list_filter = ('genre', 'format', 'author')

@admin.register(SoundDesigner)
class SoundDesignerAdmin(ImportExportModelAdmin):
    list_display = ('pk','name', 'surname', 'nickname', 'sex', 'display_balance', 'services_list')

    def display_balance(self, obj):
        return "$" + str(obj.balance)
    display_balance.short_description = 'Баланс'

    def services_list(self, obj):
        return format_html_join(', ', '<a href="{}">{}</a>', ((service.id, service.name) for service in obj.services.all()))
    services_list.short_description = 'Услуги'

    search_fields = ('name','surname','nickname')
    list_filter = ('sex',)
    ordering = ('pk',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'display_cost')
    def display_cost(self, obj):
        return "$" + str(obj.cost)
    display_cost.short_description = 'Стоимость'
    ordering = ('pk',)

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
@admin.register(ShopCart)
class ShopCartAdmin(admin.ModelAdmin):
    list_display= ('id', 'artist', 'display_sum','display_services')
    inlines = [CartItemInline]
    readonly_fields = ('sum',)

    def display_sum(self, obj):
        return "$" + str(obj.sum)
    display_sum.short_description = 'Сумма'
    def display_services(self, obj):
        return ', '.join([item.service.name for item in obj.items.all()])
    display_services.short_description = 'Услуги'   
    def save_model(self, request, obj, form, change):
        # calculate the sum
        obj.sum = sum(item.service.cost * item.quantity for item in obj.items.all())
        super().save_model(request, obj, form, change)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'cart')


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display= ('pk','name',)
    ordering = ('pk',)