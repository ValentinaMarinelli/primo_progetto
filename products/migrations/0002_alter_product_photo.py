# Generated by Django 4.2.5 on 2024-05-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.URLField(blank=True, null=True),
        ),
    ]