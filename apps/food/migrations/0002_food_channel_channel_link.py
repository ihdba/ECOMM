# Generated by Django 5.0.7 on 2024-07-15 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_channel',
            name='channel_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
