# Generated by Django 5.0.3 on 2024-04-08 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_movie_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('action', 'ACTION'), ('sci-fi', 'SCI-FI'), ('comedy', 'COMEDY'), ('thriller', 'THRILLER'), ('horror', 'HORROR'), ('drama', 'DRAMA'), ('war', 'WAR'), ('historic', 'HISTORIC'), ('documentary', 'DOCUMENTARY'), ('fantasy', 'FANTASY'), ('crime', 'CRIME'), ('music', 'MUSIC'), ('romance', 'ROMANCE'), ('animation', 'ANIMATION'), ('adventure', 'ADVENTURE'), ('mystery', 'MYSTERY'), ('survival', 'SURVIVAL')], max_length=20),
        ),
    ]