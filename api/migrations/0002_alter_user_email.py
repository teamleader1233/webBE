# Generated by Django 4.2.3 on 2023-07-22 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]
