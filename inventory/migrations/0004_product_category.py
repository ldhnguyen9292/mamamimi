# Generated by Django 5.1.4 on 2024-12-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_order_updated_at_product_created_at_product_mass_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('vegetable', 'vegetable'), ('meat', 'meat'), ('set', 'set')], default='vegetable', max_length=50),
        ),
    ]
