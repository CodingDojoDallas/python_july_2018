# Generated by Django 2.0.7 on 2018-07-20 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180720_1438'),
        ('quotes', '0002_quote_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quote_likes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_for_quote', to='quotes.Quote')),
                ('user_likes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_from_user', to='users.User')),
            ],
        ),
    ]
