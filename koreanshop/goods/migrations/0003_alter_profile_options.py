# Generated by Django 4.2.4 on 2023-09-20 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Покупатель', 'verbose_name_plural': 'Покупатели'},
        ),
    ]
