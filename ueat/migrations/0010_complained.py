# Generated by Django 4.0.6 on 2022-08-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ueat', '0009_alter_product_prod_subcategory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complained',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address1', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('product', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=12)),
                ('complaint', models.TextField(max_length=500)),
            ],
        ),
    ]