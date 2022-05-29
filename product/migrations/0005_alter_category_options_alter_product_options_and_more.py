# Generated by Django 4.0.4 on 2022-05-29 03:09

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='date_added',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('created_at',)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique_with=('created_at',)),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/thumbnails/'),
        ),
    ]