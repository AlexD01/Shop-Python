# Generated by Django 3.2.8 on 2021-12-14 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]