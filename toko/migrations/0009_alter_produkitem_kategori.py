# Generated by Django 4.2 on 2023-07-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toko', '0008_alter_alamatpengiriman_options_payment_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkitem',
            name='kategori',
            field=models.CharField(choices=[('S', 'Skincare'), ('BB', 'Bath and Body'), ('OW', 'Others')], max_length=2),
        ),
    ]