# Generated by Django 2.2.6 on 2019-10-11 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_auto_20191011_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster_url',
            field=models.URLField(),
        ),
    ]
