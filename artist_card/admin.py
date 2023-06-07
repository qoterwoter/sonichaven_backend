from .models import Song, Release, Artist
from django.contrib import admin
from .models import Song
from .utils import get_playcounts
import locale
from django.db.models import F, Sum
from import_export.admin import ImportExportModelAdmin


def update_playcounts(modeladmin, request, queryset):
    for song in queryset:
        artist_name = song.artist.name
        track_name = song.title
        song.playcounts = get_playcounts(artist_name, track_name)
        song.save()


update_playcounts.short_description = ('Обновить количество прослушиваний')


class SongAdmin(ImportExportModelAdmin):
    list_display = ('title', 'artist', 'release', 'duration', 'track_number', 'playcounts', 'pk')
    list_filter = ('release',)
    search_fields = ('title', 'artist__name', 'artist__bio', 'release__title', 'release__type', 'playcounts')
    actions = [update_playcounts]


admin.site.register(Song, SongAdmin)


class SongInline(admin.TabularInline):
    model = Song
    extra = 1
    fields = ('track_number', 'title', 'duration', 'artist', 'featuring', 'playcounts')


def update_listens(self, request, queryset):
    for release in queryset:
        for song in release.songs.all():
            song.save()
        release.get_total_listens()
        release.save()


update_listens.short_description = 'Обновить количество прослушиваний'


class ReleaseAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'artist','status', 'release_date', 'listens')
    list_filter = ['artist', 'status']
    inlines = [SongInline]
    search_fields = ('title', 'artist__name')
    can_delete = True
    actions = [update_listens]

    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'image', 'release_date', 'type', 'status')
        }),
    )


admin.site.register(Release, ReleaseAdmin)


class ArtistAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'display_payment', 'bio', 'user')
    search_fields = ('name', 'bio')
    readonly_fields = ('payment',)
    actions = ['recalculate_payment']

    def display_payment(self, obj):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
        payment_str = locale.format_string('%.2f', obj.payment, grouping=True)
        return '{} руб.'.format(payment_str)
    display_payment.short_description = 'Выплата'

    def recalculate_payment(self, request, queryset):
        for artist in queryset:
            artist.update_payment()
            artist.save()
        self.message_user(request, ('Выплаты были пересчитаны изсходя из прослушиваний артистов.'))
    recalculate_payment.short_description = ('Пересчитать выплаты для выбранных артистов')


admin.short_description = ('Пересчитать выплаты для выбранных артистов')

admin.site.register(Artist, ArtistAdmin)
