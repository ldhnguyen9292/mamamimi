# Generated by Django 5.1.4 on 2024-12-19 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_product_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]