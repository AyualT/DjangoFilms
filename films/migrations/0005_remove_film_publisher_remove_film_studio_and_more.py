# Generated by Django 4.2.1 on 2023-06-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_alter_film_options_film_is_active_alter_film_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='publisher',
        ),
        migrations.RemoveField(
            model_name='film',
            name='studio',
        ),
        migrations.AddField(
            model_name='film',
            name='distributed_by',
            field=models.CharField(max_length=100, null=True, verbose_name='Распространитель'),
        ),
    ]