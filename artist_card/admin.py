from .models import Song, Release, Artist
from django.contrib import admin
from .models import Song
from .utils import get_playcounts
import locale
from django.db.models import F, Sum


def update_playcounts(modeladmin, request, queryset):
    for song in queryset:
        artist_name = song.artist.name
        track_name = song.title
        song.playcounts = get_playcounts(artist_name, track_name)
        song.save()


update_playcounts.short_description = ('Обновить количество прослушиваний')


class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release', 'duration', 'track_number', 'playcounts')
    actions = [update_playcounts]


admin.site.register(Song, SongAdmin)


class SongInline(admin.TabularInline):
    model = Song
    extra = 1
    fields = ('track_number', 'title', 'duration', 'artist')


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'artist','status', 'release_date', 'listens')
    list_filter = ['artist']
    inlines = [SongInline]
    search_fields = ('title', 'artist__name')
    can_delete = True

    fieldsets = (
        (None, {
            'fields': ('title', 'artist', 'image', 'release_date', 'type', 'status')
        }),
    )

    actions = ['update_listens']

    def update_listens(self, request, queryset):
        for release in queryset:
            total_playcounts = release.songs.aggregate(total_playcounts=Sum('playcounts'))['total_playcounts'] or 0
            Release.objects.filter(pk=release.pk).update(listens=total_playcounts)
        self.message_user(request, f'Прослушивания обновлены для {queryset.count()} релизов.')

    update_listens.short_description = 'Обновить количество прослушиваний'

admin.site.register(Release, ReleaseAdmin)


class ArtistAdmin(admin.ModelAdmin):
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
