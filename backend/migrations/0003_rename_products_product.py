# Generated by Django 4.1.7 on 2023-02-26 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_category_image_alter_products_category_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
