# Generated by Django 3.2.8 on 2021-12-14 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20211214_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='login',
            field=models.CharField(default='', max_length=999),
        ),
    ]
