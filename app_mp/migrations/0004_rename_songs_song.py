# Generated by Django 5.0.4 on 2024-05-11 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_mp', '0003_songs_delete_playlistentry_delete_song'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='songs',
            new_name='song',
        ),
    ]