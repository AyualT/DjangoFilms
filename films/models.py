from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from actors.models import Actor
from studios.models import Studio

from hitcount.models import HitCount
from hitcount.models import HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Genre(models.Model):
    genre = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.genre
    
    class Meta:
        verbose_name = 'Жанры'
        verbose_name_plural = 'Жанры'

class Film(models.Model, HitCountMixin):
    title = models.CharField(max_length=200, verbose_name='Название фильма')
    poster = models.ImageField(upload_to='film_posters', null=True, verbose_name='Постер')
    trailer_url = models.URLField(max_length=200,null=True, verbose_name='Трейлер')
    studio = models.ForeignKey(Studio,on_delete=models.PROTECT,null=True, verbose_name='Студия')
    release_date = models.DateField(verbose_name='Дата выхода')
    distributed_by = models.CharField(max_length=100,null=True, verbose_name='Распространитель')
    director = models.CharField(max_length=100, verbose_name='Директор')
    stars = models.ManyToManyField(Actor, verbose_name='Актеры')
    genre = models.ManyToManyField(Genre, verbose_name='Жанр')
    desc = models.TextField(verbose_name='Описание')
    budget = models.PositiveIntegerField(
        'Бюджет', default=0, help_text='указывать сумму в долларах'
        )
    gross_worldwide = models.PositiveIntegerField(
        'Сборы в мире', default=0, help_text='указывать сумму в долларах'
        )
    rating_IMDb = models.FloatField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(10.0)
        ], verbose_name='Рейтинг IMDb'
    )

    is_active = models.BooleanField(default=True)

    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def current_hitcount(self):
        return self.hit_count.hits

    def current_hitcount_in_last_day(self):
        return self.hit_count.hits_in_last(days=1)

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('film_detail',args=[str(self.id)])

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-release_date','title']

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    rating_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    rating_choise = (
        (0,0),
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    rating = models.IntegerField(choices=rating_choise, default=0, verbose_name='Рейтинг')
    comment = models.TextField(verbose_name='Комментарий')
    film = models.ForeignKey(Film, on_delete=models.CASCADE, verbose_name='Фильм')

    def __str__(self):
        return f'{self.film.title} by {self.author}'
    
    class Meta:
        verbose_name = 'Комментарии и оценка'
        verbose_name_plural = 'Комментарии и оценка'
    
class ReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    value_choise = (
        (0,0),
        (1,1)
    )
    value = models.IntegerField(choices=value_choise)

    def __str__(self):
        return f'Review:{self.review} | User: {self.user} | Value: {self.value}'
    
    class Meta:
        verbose_name = 'Лайки к комментариям'
        verbose_name_plural = 'Лайки к комментариям'
    
