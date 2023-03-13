from django.db import models
from datetime import timedelta
from artist_card.models import Artist

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name

class SoundDesigner(models.Model):
    SEX_CHOICES = [
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    ]
    name = models.CharField('Имя',max_length=50)
    surname = models.CharField('Фамилия',max_length=50)
    nickname = models.CharField('Псеводним',max_length=50, unique=True)
    sex = models.CharField('Пол',max_length=1, choices=SEX_CHOICES)
    balance = models.DecimalField('Баланс',max_digits=8, decimal_places=2,default=0)

    class Meta:
        verbose_name = 'Звукоржессер'
        verbose_name_plural = 'Звукоржессеры'

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Arrangement(models.Model):
    FORMAT_CHOICES = [
        ('wav', 'WAV'),
        ('mp3', 'MP3'),
        ('flac', 'FLAC'),
        ('aac', 'AAC'),
        ('dsd', 'DSD'),
    ]
    title = models.CharField('Название',max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='arrangements')
    duration = models.DurationField('Длительность',default=timedelta(minutes=0))
    cost = models.DecimalField('Стоимость (RUB)',max_digits=8, decimal_places=2)
    format = models.CharField('Формат',max_length=4, choices=FORMAT_CHOICES)
    author = models.ForeignKey(SoundDesigner, on_delete=models.CASCADE, related_name='arrangements', verbose_name='Автор')

    class Meta:
        verbose_name = 'Арранжировка'
        verbose_name_plural = 'Арранжировки'

    def __str__(self):
        return f"{self.genre} - {self.author}"

class Service(models.Model):
    TYPE_CHOICES = [
        ('C', 'Композиция'),
        ('P', 'Производство'),
        ('M', 'Сведение'),
        ('M+', 'Сведение и Мастеринг'),
        ('D', 'Дистрибуция'),
    ]
    name = models.CharField('Название',max_length=100)
    cost = models.DecimalField('Стоимость',max_digits=8, decimal_places=2)
    type = models.CharField('Тип',max_length=2, choices=TYPE_CHOICES)
 
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.cost}"


class ShopCart(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='carts',verbose_name='Клиент')
    sum = models.DecimalField('Сумма заказа', max_digits=10, decimal_places=2, default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.artist.name} - {self.sum}'

class CartItem(models.Model):
    quantity = models.PositiveIntegerField('Количество',default=1)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE, related_name='items')
    
    class Meta:
        verbose_name = 'Позиция в корзине'
        verbose_name_plural = 'Позиции в корзине'
