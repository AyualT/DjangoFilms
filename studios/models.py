from django.db import models
from django.urls import reverse

from hitcount.models import HitCount
from hitcount.models import HitCountMixin
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.

class Studio(models.Model, HitCountMixin):
    name = models.CharField(max_length=100, verbose_name='Название студии')
    logo = models.ImageField(upload_to='studio_logos',null=True, verbose_name='Логотип')
    headquarters = models.CharField(max_length=100, verbose_name='Расположение')
    founder = models.CharField(max_length=200, verbose_name='Основатели')
    founded = models.DateField(verbose_name='Основание')
    films = models.TextField(verbose_name='Фильмы')
    main_site = models.URLField(max_length=200, verbose_name='Сайт студии')
    is_active = models.BooleanField(default=True, null=True)

    hit_count_generic = GenericRelation(
        HitCount, 
        object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    def current_hitcount(self):
        return self.hit_count.hits

    def current_hitcount_in_last_day(self):
        return self.hit_count.hits_in_last(days=1)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return reverse('studio_detail',args=[str(self.id)])
    
    class Meta:
        verbose_name = 'Студии'
        verbose_name_plural = 'Студии'