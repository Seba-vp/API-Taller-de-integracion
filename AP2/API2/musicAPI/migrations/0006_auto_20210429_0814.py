# Generated by Django 3.2 on 2021-04-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPI', '0005_auto_20210428_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artist_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='cancion',
            name='album_id',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='cancion',
            name='artist_id',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
