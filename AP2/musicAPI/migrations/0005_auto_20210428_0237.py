# Generated by Django 3.2 on 2021-04-28 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicAPI', '0004_auto_20210428_0200'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='self',
            new_name='Self',
        ),
        migrations.RenameField(
            model_name='artista',
            old_name='self',
            new_name='Self',
        ),
        migrations.RenameField(
            model_name='cancion',
            old_name='self',
            new_name='Self',
        ),
    ]
