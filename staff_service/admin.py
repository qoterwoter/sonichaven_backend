from django.contrib import admin
from .models import Arrangement, SoundEngineer, Service, ShopCart, CartItem, Genre, Contract, Manager, Order, OrderItem
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.html import format_html_join
from django import forms
from django.contrib.auth.models import User


class ManagerAdminForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].queryset = User.objects.filter(is_active=True, is_staff=True, is_superuser=False)


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    form = ManagerAdminForm
    list_display = ('user', 'enjoy_date', 'display_payment')
    search_fields = ['user', 'payment']

    def display_payment(self, obj):
        return str(obj.payment) + " Руб"

    display_payment.short_description = 'Зарплата'


@admin.register(Arrangement)
class ArrangementAdmin(admin.ModelAdmin):
    list_display = ('genre', 'duration', 'cost', 'format', 'author')
    list_filter = ('genre', 'format', 'author')


@admin.register(SoundEngineer)
class SoundDesignerAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name', 'surname', 'nickname', 'sex', 'display_balance', 'services_list')

    def display_balance(self, obj):
        return "Руб" + str(obj.balance)

    display_balance.short_description = 'Баланс'

    def services_list(self, obj):
        return format_html_join(', ', '<a href="{}">{}</a>',
                                ((service.id, service.name) for service in obj.services.all()))

    services_list.short_description = 'Услуги'

    search_fields = ('name', 'surname', 'nickname')
    list_filter = ('sex',)
    ordering = ('pk',)


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name', 'display_cost', 'description')
    search_fields = ('name',)
    list_filter = ('type',)

    def display_cost(self, obj):
        return str(obj.cost) + " руб."

    display_cost.short_description = 'Стоимость'
    ordering = ('pk',)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(ShopCart)
class ShopCartAdmin(ImportExportModelAdmin):
    list_display = ('id', 'artist', 'display_sum', 'display_services')
    inlines = [CartItemInline]
    readonly_fields = ('sum',)

    def display_sum(self, obj):
        return str(obj.sum) + ' Руб.'

    display_sum.short_description = 'Сумма'

    def display_services(self, obj):
        return ', '.join([item.service.name for item in obj.items.all()])

    display_services.short_description = 'Услуги'

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        # calculate the sum
        obj.sum = sum(item.service.cost * item.quantity for item in obj.items.all())
        obj.save()


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('service', 'pk', 'quantity', 'cart')


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'title',)
    search_fields = ('title',)
    ordering = ('pk',)


class ContractAdmin(admin.ModelAdmin):
    list_display = ('artist', 'signing_date', 'duration', 'contract_terms',)
    search_fields = ('artist__name',)
    list_filter = ('signing_date',)
    date_hierarchy = 'signing_date'


admin.site.register(Contract, ContractAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'created_at')
    inlines = [OrderItemInline, ]
    list_filter = ('created_at',)
    search_fields = ('cart__artist__name',)


admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'service')


admin.site.register(OrderItem, OrderItemAdmin)
