# Generated by Django 3.2.8 on 2021-12-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='section',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='storage',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
