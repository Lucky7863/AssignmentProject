# Generated by Django 4.1.1 on 2022-09-22 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BooksApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='pubished',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='books',
            old_name='pubisher',
            new_name='publisher',
        ),
    ]
