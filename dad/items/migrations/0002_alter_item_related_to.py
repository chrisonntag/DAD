# Generated by Django 3.2.16 on 2023-01-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='related_to',
            field=models.ManyToManyField(blank=True, related_name='_items_item_related_to_+', to='items.Item'),
        ),
    ]