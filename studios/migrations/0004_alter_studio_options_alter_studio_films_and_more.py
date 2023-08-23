# Generated by Django 4.2.1 on 2023-07-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studios', '0003_studio_is_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studio',
            options={'verbose_name': 'Студии', 'verbose_name_plural': 'Студии'},
        ),
        migrations.AlterField(
            model_name='studio',
            name='films',
            field=models.TextField(verbose_name='Фильмы'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='founded',
            field=models.DateField(verbose_name='Основание'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='founder',
            field=models.CharField(max_length=200, verbose_name='Основатели'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='headquarters',
            field=models.CharField(max_length=100, verbose_name='Расположение'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='logo',
            field=models.ImageField(null=True, upload_to='studio_logos', verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='main_site',
            field=models.URLField(verbose_name='Сайт студии'),
        ),
        migrations.AlterField(
            model_name='studio',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название студии'),
        ),
    ]