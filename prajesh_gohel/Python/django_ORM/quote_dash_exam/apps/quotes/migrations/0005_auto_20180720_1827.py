# Generated by Django 2.0.7 on 2018-07-20 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0004_auto_20180720_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='likes',
            field=models.IntegerField(),
        ),
    ]