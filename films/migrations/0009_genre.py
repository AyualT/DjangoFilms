# Generated by Django 4.2.1 on 2023-07-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_alter_review_rating_reviewlike'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
    ]
