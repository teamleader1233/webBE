# Generated by Django 4.2.4 on 2023-08-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_v2', '0002_bill_note_bill_precollected_price_bill_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.UUIDField(db_index=True, default='Zv_pJsfHEPM', editable=False, primary_key=True, serialize=False),
        ),
    ]
