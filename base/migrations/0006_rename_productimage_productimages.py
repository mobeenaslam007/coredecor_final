# Generated by Django 3.2 on 2021-05-20 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_product_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductImage',
            new_name='ProductImages',
        ),
    ]