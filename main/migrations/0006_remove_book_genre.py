# Generated by Django 3.1.4 on 2021-01-23 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_book_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
    ]
