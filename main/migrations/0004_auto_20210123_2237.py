# Generated by Django 3.1.4 on 2021-01-23 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20210123_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
