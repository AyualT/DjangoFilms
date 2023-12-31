# Generated by Django 4.2.1 on 2023-06-12 20:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_film_trailer_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['-release_date', 'title'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AddField(
            model_name='film',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='film',
            name='director',
            field=models.CharField(max_length=100, verbose_name='Директор'),
        ),
        migrations.AlterField(
            model_name='film',
            name='genre',
            field=models.CharField(max_length=100, verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(null=True, upload_to='film_posters', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='film',
            name='publisher',
            field=models.CharField(max_length=100, verbose_name='Издатель'),
        ),
        migrations.AlterField(
            model_name='film',
            name='rating_IMDb',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='Рейтинг IMDb'),
        ),
        migrations.AlterField(
            model_name='film',
            name='release_date',
            field=models.DateField(verbose_name='Дата выхода'),
        ),
        migrations.AlterField(
            model_name='film',
            name='stars',
            field=models.CharField(max_length=100, verbose_name='Актеры'),
        ),
        migrations.AlterField(
            model_name='film',
            name='studio',
            field=models.CharField(max_length=100, verbose_name='Студия'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название фильма'),
        ),
        migrations.AlterField(
            model_name='film',
            name='trailer_url',
            field=models.URLField(null=True, verbose_name='Трейлер'),
        ),
    ]
