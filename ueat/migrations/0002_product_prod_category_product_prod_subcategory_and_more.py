# Generated by Django 4.0.6 on 2022-08-04 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ueat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='prod_subcategory',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
