# Generated by Django 5.0.3 on 2024-04-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_movie_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='leadrole',
            new_name='actor',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='writter',
            new_name='actress',
        ),
        migrations.RemoveField(
            model_name='item',
            name='actor1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='actor2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='actor3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='actor4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='actor5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='episodes',
        ),
        migrations.RemoveField(
            model_name='item',
            name='seasons',
        ),
        migrations.AlterField(
            model_name='category',
            name='discription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='summary',
            field=models.TextField(),
        ),
    ]