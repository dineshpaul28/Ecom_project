# Generated by Django 4.0.6 on 2022-08-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ueat', '0010_complained'),
    ]

    operations = [
        migrations.AddField(
            model_name='complained',
            name='phone',
            field=models.CharField(max_length=12, null=True),
        ),
    ]