# Generated by Django 5.1.4 on 2024-12-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_product_set_products_alter_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('g', 'g'), ('con', 'con'), ('ml', 'ml')], default='g', max_length=50),
        ),
    ]