# Generated by Django 4.2.1 on 2023-07-20 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0011_film_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанры', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Комментарии и оценка', 'verbose_name_plural': 'Комментарии и оценка'},
        ),
        migrations.AlterModelOptions(
            name='reviewlike',
            options={'verbose_name': 'Лайки к комментариям', 'verbose_name_plural': 'Лайки к комментариям'},
        ),
    ]
