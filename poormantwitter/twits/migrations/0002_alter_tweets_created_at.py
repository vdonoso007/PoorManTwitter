# Generated by Django 3.2.8 on 2021-10-08 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twits', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='created_at',
            field=models.DateTimeField(auto_created=True),
        ),
    ]
